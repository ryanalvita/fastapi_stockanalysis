from fastapi import APIRouter

from model import Report, ReportType
from view import ReportAPI

router = APIRouter()


@router.get("/{report_type}/all", response_model=Report)
async def report_all(report_type: ReportType):
    reports = await ReportAPI.get_report_all(report_type)
    return [Report(**report) for report in reports]


@router.get("/{report_type}/{stock_code}", response_model=Report)
async def report_stock_code(report_type: ReportType, stock_code: str):
    report = await ReportAPI.get_report_code(report_type, stock_code)
    return Report(**report)
