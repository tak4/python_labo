from sample_pydoc.sample_pydoc import total_amount_restructure_text_style

def test_sample():
    """テスト"""
    pass

def test_total_amount_restructure_text_style():
    """total_amount_restructure_text_styleのテスト
    
    """
    sum = total_amount_restructure_text_style(1000, 100, 0.1)

    assert sum == 1210, 'sum error'
