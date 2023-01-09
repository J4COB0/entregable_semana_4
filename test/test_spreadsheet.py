import pandas as pd

def coon_pool_to_google_spreadsheet(sheet_id):
    """
    This functions form the route adding the sheet id
    """
    return f'https://docs.google.com/spreadsheets/u/0/d/{sheet_id}/export?format=csv&id={sheet_id}&gid=987275882'

def test_coon_pool_to_google_spreadsheet_is_ok():
    """
    This functions is used to test if the operatios is successfully, using pandas to read a spreadsheet
    """    
    sheet_id = '1wRVoUiLhDmchtiVRhwR2aeYNz2crWrO5'
    url = coon_pool_to_google_spreadsheet(sheet_id=sheet_id)
    df = pd.read_csv(url)

    # TESTING THE AMOUNT, THE AMOUNT HAVE TO BE DIFFERENT TO 0
    assert len(df) != 0
    