import cot_reports as cot
import datetime as dt
import pandas as pd
import plotly.express as px

# 定数
DATE_COL = "As of Date in Form YYYY-MM-DD"
YEN_MARKET = "JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE"
OUTPUT_HTML = "docs/yen_cot.html"


def fetch_cot_data(start_year=2017):
    """COTデータを1986年から現在まで取得し連結する"""
    years = range(start_year, dt.datetime.now().year + 1)
    reports = [cot.cot_year(year=year) for year in years]
    reports.append(cot.cot_hist(cot_report_type="legacy_fut"))
    report = pd.concat(reports, ignore_index=True)
    report[DATE_COL] = pd.to_datetime(report[DATE_COL])
    return report


def extract_yen_positions(report):
    """日本円のIMMデータのみ抽出し、必要なカラムとNet計算を行う"""
    yen_report = report[report['Market and Exchange Names'] == YEN_MARKET]
    yen_df = yen_report.sort_values(DATE_COL, ascending=True).reset_index(drop=True)[
        [DATE_COL, 'Noncommercial Positions-Long (All)', 'Noncommercial Positions-Short (All)']
    ]
    yen_df['Net Noncommercial Positions'] = (
        yen_df['Noncommercial Positions-Long (All)'] - yen_df['Noncommercial Positions-Short (All)']
    )
    return yen_df


def plot_yen_positions(yen_df, output_path=OUTPUT_HTML):
    """Net非商業ポジションの推移をプロットしHTML出力"""
    fig = px.line(
        yen_df,
        x=DATE_COL,
        y="Net Noncommercial Positions",
        title="Net Noncommercial Yen Positions Over Time; IMM(International Monetary Market) Data",
        labels={DATE_COL: "Date", "Net Noncommercial Positions": "Net Noncommercial Positions"}
    )
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="date"
        )
    )
    fig.write_html(output_path)


def main():
    report = fetch_cot_data()
    yen_df = extract_yen_positions(report)
    plot_yen_positions(yen_df)


if __name__ == "__main__":
    main()
