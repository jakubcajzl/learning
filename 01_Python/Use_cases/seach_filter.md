The best way to write a search filter over a DataFrame in Python depends on your specific requirements, including the size of your DataFrame, the complexity of your search criteria, and the performance considerations.

However, here are some common approaches:

1. **Boolean Indexing**: This approach involves creating boolean masks based on your search criteria and then using these masks to filter the DataFrame. It's straightforward and efficient for simple filtering tasks.

    ```python
    filtered_df = df[df['column_name'] == 'search_criteria']
    ```

2. **Using `.query()`**: Pandas provides a `.query()` method that allows you to filter DataFrames using a query string syntax similar to SQL. This can be convenient for complex filtering operations.

    ```python
    filtered_df = df.query("column_name == 'search_criteria' and another_column > 10")
    ```

3. **Using `.loc[]` or `.iloc[]`**: You can use the `.loc[]` or `.iloc[]` accessor to filter rows based on index labels or integer location. This approach is useful if you need to filter rows based on their position or based on multiple conditions.

    ```python
    filtered_df = df.loc[(df['column_name'] == 'search_criteria') & (df['another_column'] > 10)]
    ```

4. **Using Custom Functions**: For more complex filtering logic, you can define custom functions and apply them to the DataFrame using methods like `.apply()` or `.applymap()`.

    ```python
    def custom_filter(row):
        return row['column_name'] == 'search_criteria' and row['another_column'] > 10

    filtered_df = df[df.apply(custom_filter, axis=1)]
    ```

5. **Combining Methods**: You can combine multiple filtering methods to achieve the desired result. For example, you can use boolean indexing along with `.loc[]` or `.query()` for more complex conditions.

    ```python
    filtered_df = df.loc[df['column_name'] == 'search_criteria'].query("another_column > 10")
    ```

Choose the approach that best suits your requirements in terms of readability, performance, and flexibility. Additionally, consider the size and structure of your DataFrame when selecting a filtering method, as some methods may be more efficient than others for large datasets.