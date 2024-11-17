def test_category_init(first_category, second_category):
    assert first_category.name == "Phone"
    assert first_category.description == "smt des phone"
    assert len(first_category.products) == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3
    assert first_category.category_count == 2
