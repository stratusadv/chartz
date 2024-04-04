# chartz
Python echarts wrapper

```python

def price_vs_projected_line_chart(ticker: str):
    mpg_data = MpgPrice.objects.filter(ticker='CIX')
    dimensions = ('date', 'price', 'projected_price')
    x_axis = [mpg.reference_date.strftime('%d-%m-%y') for mpg in mpg_data]
    price_data = [float(mpg.price) for mpg in mpg_data]
    projected_price = [float(mpg.projected_price) for mpg in mpg_data]
    dataset = list(zip(x_axis, price_data, projected_price))
    dataset.insert(0, dimensions)

    line_chart = Chart(title='CIX', height=375)

    line_chart.y_axis.name = 'Price'
    line_chart.x_axis.name = 'Time'

    line_chart.hide_legend()
    line_chart.hide_title()

    line_chart.add_dataset(data=dataset)

    price_series = line_chart.add_series(chart_type='line', show_labels=False)
    price_series.configure(x_axis='date', y_axis='price')

    projected_price_series = line_chart.add_series(chart_type='line', show_labels=False)
    projected_price_series.configure(x_axis='date', y_axis='projected_price')

    return line_chart.to_dict()


def tsx_sector_echart():
    sectors = Sector.objects.all().order_by('name')
    companies = Company.objects.all().order_by('sector__name').prefetch_related('sector')
    labels = [sector.name for sector in sectors]
    counter = Counter([company.sector.name for company in companies])
    sector_data = list(zip(labels, [counter[sector.name] for sector in sectors]))
    sector_data.insert(0, ('Sector', 'Companies'))

    pie_echart = echart.Chart(
        title='Companies by Sector',
        height=275,
    )

    pie_echart.hide_axis()
    pie_echart.hide_title()

    pie_echart.position_legend(orientation='vertical', left='left')

    pie_echart.add_dataset(sector_data)

    pie_series = pie_echart.add_series('pie', show_labels=False)
    pie_series.position_chart('70%', '50%')
    pie_series.radius = '70%'

    return pie_echart.to_dict()



```