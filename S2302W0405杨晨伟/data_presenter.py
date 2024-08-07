import os
import data_plotter

companies = []
plotters = {}
start_year = 2014


def main():
    __init_data()
    for company in companies:
        make_summary(company)
    print("Done!")


def make_summary(company_name):
    plotter = plotters[company_name]

    plotter.show_whole_time_series()
    plotter.show_time_series(start_year=start_year, end_year=2022)
    plotter.show_preprocessed_prices(start_year=start_year, end_year=2022)
    plotter.show_gp_prediction(train_start=start_year, train_end=2022, pred_year=2023)
    plotter.show_time_series(start_year=start_year, end_year=2024)
    plotter.show_gp_prediction(train_start=start_year, train_end=2024, pred_year=2024, pred_quarters=[3, 4])
    print(company_name + ' summary done!')


def __init_data():
    for company in os.listdir('Data'):
        current_company = company.split('.')[0]
        companies.append(current_company)
        plotters[current_company] = (data_plotter.Plotter(company_name=current_company))


if __name__ == "__main__":
    main()
