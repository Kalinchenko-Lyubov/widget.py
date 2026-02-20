from src.file_readers import transactions_from_csv, transactions_from_excel
import pandas as pd


def test_valid_csv(mocker, sample_df):
    mocker.patch.object(pd, "read_csv", return_value=sample_df)
    path = "/fake/path/to/file.csv"
    result = transactions_from_csv(path)
    assert isinstance(result, list)
    assert len(result) > 0
    first_record = result[0]
    assert set(first_record.keys()) == {
        "id",
        "state",
        "date",
        "amount",
        "currency_name",
        "currency_code",
        "from",
        "to",
        "description",
    }


def test_file_not_found(mocker):
    mocker.patch.object(pd, "read_csv", side_effect=FileNotFoundError())
    path = "/nonexistent/path/to/file.csv"
    result = transactions_from_csv(path)
    assert result is None


def test_empty_data_error(mocker):
    mocker.patch.object(pd, "read_csv", side_effect=pd.errors.EmptyDataError())
    path = "/empty/data/file.csv"
    result = transactions_from_csv(path)
    assert result is None


def test_parser_error(mocker):
    mocker.patch.object(pd, "read_csv", side_effect=pd.errors.ParserError())
    path = "/invalid/format/file.csv"
    result = transactions_from_csv(path)
    assert result is None


def test_general_exception(mocker):
    mocker.patch.object(pd, "read_csv", side_effect=Exception("Some unknown exception"))
    path = "/some/path/file.csv"
    result = transactions_from_csv(path)
    assert result is None


def test_valid_excel(mocker, sample_df):
    mocker.patch.object(pd, "read_excel", return_value=sample_df)
    path = "/fake/path/to/excel.xlsx"
    result = transactions_from_excel(path)
    assert isinstance(result, list)
    assert len(result) > 0
    first_record = result[0]
    assert set(first_record.keys()) == {
        "id",
        "state",
        "date",
        "amount",
        "currency_name",
        "currency_code",
        "from",
        "to",
        "description",
    }


def test_file_not_found_excel(mocker):
    mocker.patch.object(pd, "read_excel", side_effect=FileNotFoundError())
    path = "/nonexistent/path/to/excel.xlsx"
    result = transactions_from_excel(path)
    assert result is None


def test_empty_data_error_excel(mocker):
    mocker.patch.object(pd, "read_excel", side_effect=pd.errors.EmptyDataError())
    path = "/empty/data/excel.xlsx"
    result = transactions_from_excel(path)
    assert result is None


def test_parser_error_excel(mocker):
    mocker.patch.object(pd, "read_excel", side_effect=pd.errors.ParserError())
    path = "/invalid/format/excel.xlsx"
    result = transactions_from_excel(path)
    assert result is None


def test_general_exception_excel(mocker):
    mocker.patch.object(pd, "read_excel", side_effect=Exception("Some unknown exception"))
    path = "/some/path/excel.xlsx"
    result = transactions_from_excel(path)
    assert result is None
