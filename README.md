# bl_loc_summaries

Collect Google Map summary information from locations. 

Input: A CSV file of locations (contains a name column and address column)

Output: A CSV file of summary information for all locations

## Installation

```python
pip install bl_loc_summaries
```


## Functions

1. **run_scraper()**
```python
bl_loc_summaries.run_scraper(input_path, name_col, address_col,
				scrapers, window)
```

run_scraper() starts the scraping process. CSVs of location summary information
are added one-by-one to the generated ```outputs``` folder. 

Parameters:

* input_path: String, the path to a CSV file of locations.

* name_col: String, the name of the column of location names.

* address_col: String, the name of the column of location addresses.

* scrapers: Int, the number of scrapers to use, [1-18] allowed. 

* window: Bool, if True - chrome bot pop up window appears


2. **merge_outputs**
```python
bl_loc_summaries.merge_outputs(input_path)
```
merge_outputs() should be run after run_scraper(). Given the input_path, it combines
all CSVs in the ```outputs``` folder into one, saving it as ```MERGED.csv``` 
in the same folder. 


## Example

The file ```test_locations.csv``` is included for testing purposes. It contains 50
locations in Pittsburgh, PA to get summary information for. 

You can insert the following code into an IDE and run that file:

```python
import bl_loc_summaries as bl

if __name__ == "__main__":
	f = "C:/a_folder_location/test_locations.csv"
	bl.run_scraper(input_path = f, name_col = "Name", 
        	address_col = "Address")
```

The scraper should be run in an ```if __name__ == "__main__"``` to avoid multiprocessing 
errors. 

Once that is fully run (progress bar shown in terminal), you can use the following
code to create the CSV of all location summary information merged into one file.

```python
bl.merge_outputs(input_path = f)
```

After these steps, you're done! ```MERGED.csv``` is the final result. 
