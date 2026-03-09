# Video Game Sales EDA  
By James Weaver

## Introduction  
This project focuses on analyzing a video game sales dataset to uncover trends in global and regional sales performance. The dataset includes video games that sold at least 100000 copies globally and features sales across North America, Europe, Japan, and other regions. The main goal is to explore the data using streamlit.

## Files  
1. **video_game_sales_analysis.ipynb**  
   The main Jupyter Notebook containing the code for data cleaning, exploratory analysis, and visualizations.  
2. **video_game_sales.csv**  
   Dataset containing video game titles, release years, platforms, platform generations, companies, and regional sales.  
3. **README.md**  
   Overview of the project, methodology, tools used, and key findings.

## Approach  
1. **Data Exploration**  
   - Reviewed the structure of the dataset and examined both numeric and categorical variables.  
   - Summarized important columns such as year, platform, and regional sales.  
2. **Exploratory Data Analysis (EDA)**  
   - Analyzed sales trends over time by region.  
   - Examined the distribution of global sales.  
   - Compared platform companies and console performance.  
3. **Visualization**  
   - Created a histogram to show the distribution of global sales.  
   - Built a bar chart to compare yearly sales by country.  
   - Used scatterplots to examine the relationship between console/company and sales. 

## Tools Used  
- **Python**: Data cleaning, analysis, and visualization.  
- **Pandas**: Data manipulation and summary statistics.  
- **NumPy**: Numerical support for analysis.  
- **Matplotlib / Plotly**: Visualizing sales trends and relationships.

## Key Findings  
1. **Dataset Coverage**  
   - The dataset contains 9989 video games released between 1990 and 2017.   
2. **Regional Sales Trends**  
   - Average sales were highest in North America at 0.315 million, followed by Europe at 0.179 million and Japan at 0.089 million.   
3. **Top Platform Presence**  
   - The PS2 was the most common platform in the dataset, with 2127 games represented.  
4. **Game Title Frequency**  
   - There were 6925 unique game titles, with **NBA Jam** appearing most often at 7 times. 
5. **Global Sales Distribution**  
   - Most games had relatively low global sales, while a small number of titles were very large outliers, reaching over 80 million in global sales. This shows a heavily right-skewed distribution. The histogram  shows most values clustered near the low end with a long tail to the right.   
6. **Sales Over Time**  
   - The yearly bar chart shows stronger sales in North America than in Europe and Japan across many years, with visible peaks in the late 2000s. The chart on page 4 highlights this trend clearly. 
7. **Platform Company Performance**  
   - The scatterplot suggests that Nintendo includes some of the highest global-selling titles in the dataset. The chart on page 4 shows one very large outlier above 80 million global sales. 

## Visuals  
### Distribution of Global Sales  
![Distribution of Global Sales](global_sales_histogram.png)

### Video Game Sales Each Year By Country  
![Sales by Country](sales_each_year_by_country.png)

### Platform Company vs Global Sales  
![Platform Company Scatterplot](platform_company_scatterplot.png)

## Recommendations  
1. **Focus on Strong Regions**  
   - Since North America shows the highest average sales, companies may want to prioritize marketing and release strategies there.  
2. **Support Top Platforms**  
   - Because PS2 appears most frequently in the dataset, platform popularity should be considered when studying historical success.  
3. **Study High-Performing Outliers**  
   - A small number of games generate extremely high sales, so it would be valuable to investigate what these titles have in common.  
4. **Regional Strategy**  
   - Since Europe and Japan show different sales levels than North America, companies should tailor game releases and promotions by region.

## Future Improvements  
- Analyze genre level performance if genre data becomes available.  
- Compare publisher performance across regions and time periods.  
- Study how platform generation affects sales success.  
- Add more detailed visualizations.