import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import AdvancedSearchBar from "../components/advancedSearchBar";
import SearchResult from "../components/searchResult";
import Filter from "../components/filter";
import axios from "axios";

class SearchResults extends Component {
  state = {
    searchResults: [
      {
        id: 1,
        brand: "HP",
        title:
          "HP 15-DB0000AU AMD DUAL CORE E2-9000e (1.5-2.0GHz, 4GB DDR4, 500GB, DVD-RW) 15.6 Inch Black Notebook with Win-10 Home #4JN12PA",
        description: [
          "Processor - AMD DUAL CORE E2-9000e",
          "Processor Clock Speed - 1.5-2.0GHz",
          'Display Size - 15.6"',
          "RAM - 4GB",
          "RAM Type - DDR4 2400MHz",
          "Storage - 500GB HDD",
          "Operating System - Windows 10 Home"
        ],
        website: [
          {
            sitename: "Ryan",
            price: 26000,
            img_link:
              "https://ryanscomputers.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/1/5/15-db0000au.jpg",
            p_link:
              "https://ryanscomputers.com/hp-15-db0000au-amd-dual-core-e2-9000e-1-5-2-0ghz-4gb-ddr4-500gb-dvd-rw-15-6-inch-black-notebook-with-win-10-home-2-yr-warranty-4jn12pa.html",
            status: "Available"
          },
          {
            sitename: "Startech",
            price: 26500,
            img_link:
              "https://www.startech.com.bd/image/cache/catalog/laptop/hp-laptop/db0000au/db0000au-500x500.jpg",
            p_link:
              "https://www.startech.com.bd/hp-15-db0000au-amd-dual-core-laptop",
            status: "Not Available"
          }
        ]
      },
      {
        id: 2,
        brand: "Lenovo",
        title:
          'HP 15-da0023tu Pentium Quad Core 15.6" HD Laptop With Genuine WIn 10',
        description: [
          "Processor - Intel PQC N5000",
          "Processor Clock Speed - 1.1-2.7GHz",
          'Display Size - 15.6"',
          "RAM - 4GB",
          "RAM Type - DDR4",
          "Storage - 500GB HDD"
        ],
        website: [
          {
            sitename: "Ryan",
            price: 32500,
            img_link:
              "https://ryanscomputers.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/1/5/15-bs074tx-silver-2_2.jpg",
            p_link:
              "https://ryanscomputers.com/hp-15-da0023tu-intel-pqc-n5000-1-1-2-7ghz-4gb-ddr4-500gb-dvd-rw-15-6-inch-hd-1366-x-768-display-silver-notebook-with-win-10-home-4kz21pa.html",
            status: "Not Available"
          },
          {
            sitename: "Startech",
            price: 32000,
            img_link:
              "https://www.startech.com.bd/image/cache/catalog/laptop/hp-laptop/da0023tu/da0023tu-500x500.jpg",
            p_link: "https://www.startech.com.bd/hp-da0023tpqc-laptop",
            status: "Available"
          }
        ]
      }
    ],
    filterResults: [
      {
        id: 1,
        brand: "HP",
        title:
          "HP 15-DB0000AU AMD DUAL CORE E2-9000e (1.5-2.0GHz, 4GB DDR4, 500GB, DVD-RW) 15.6 Inch Black Notebook with Win-10 Home #4JN12PA",
        description: [
          "Processor - AMD DUAL CORE E2-9000e",
          "Processor Clock Speed - 1.5-2.0GHz",
          'Display Size - 15.6"',
          "RAM - 4GB",
          "RAM Type - DDR4 2400MHz",
          "Storage - 500GB HDD",
          "Operating System - Windows 10 Home"
        ],
        website: [
          {
            sitename: "Ryan",
            price: 26000,
            img_link:
              "https://ryanscomputers.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/1/5/15-db0000au.jpg",
            p_link:
              "https://ryanscomputers.com/hp-15-db0000au-amd-dual-core-e2-9000e-1-5-2-0ghz-4gb-ddr4-500gb-dvd-rw-15-6-inch-black-notebook-with-win-10-home-2-yr-warranty-4jn12pa.html",
            status: "Available"
          },
          {
            sitename: "Startech",
            price: 26500,
            img_link:
              "https://www.startech.com.bd/image/cache/catalog/laptop/hp-laptop/db0000au/db0000au-500x500.jpg",
            p_link:
              "https://www.startech.com.bd/hp-15-db0000au-amd-dual-core-laptop",
            status: "Not Available"
          }
        ]
      },
      {
        id: 2,
        brand: "Lenovo",
        title:
          'HP 15-da0023tu Pentium Quad Core 15.6" HD Laptop With Genuine WIn 10',
        description: [
          "Processor - Intel PQC N5000",
          "Processor Clock Speed - 1.1-2.7GHz",
          'Display Size - 15.6"',
          "RAM - 4GB",
          "RAM Type - DDR4",
          "Storage - 500GB HDD"
        ],
        website: [
          {
            sitename: "Ryan",
            price: 32500,
            img_link:
              "https://ryanscomputers.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/1/5/15-bs074tx-silver-2_2.jpg",
            p_link:
              "https://ryanscomputers.com/hp-15-da0023tu-intel-pqc-n5000-1-1-2-7ghz-4gb-ddr4-500gb-dvd-rw-15-6-inch-hd-1366-x-768-display-silver-notebook-with-win-10-home-4kz21pa.html",
            status: "Not Available"
          },
          {
            sitename: "Startech",
            price: 32000,
            img_link:
              "https://www.startech.com.bd/image/cache/catalog/laptop/hp-laptop/da0023tu/da0023tu-500x500.jpg",
            p_link: "https://www.startech.com.bd/hp-da0023tpqc-laptop",
            status: "Available"
          }
        ]
      }
    ],
    category: [
      { label: "Afghanistan" },
      { label: "Aland Islands" },
      { label: "Albania" },
      { label: "Algeria" },
      { label: "American Samoa" },
      { label: "Andorra" },
      { label: "Angola" },
      { label: "Anguilla" },
      { label: "Antarctica" },
      { label: "Antigua and Barbuda" },
      { label: "Argentina" },
      { label: "Armenia" },
      { label: "Aruba" },
      { label: "Australia" },
      { label: "Austria" },
      { label: "Azerbaijan" },
      { label: "Bahamas" },
      { label: "Bahrain" },
      { label: "Bangladesh" },
      { label: "Barbados" },
      { label: "Belarus" },
      { label: "Belgium" },
      { label: "Belize" },
      { label: "Benin" },
      { label: "Bermuda" },
      { label: "Bhutan" },
      { label: "Bolivia, Plurinational State of" },
      { label: "Bonaire, Sint Eustatius and Saba" },
      { label: "Bosnia and Herzegovina" },
      { label: "Botswana" },
      { label: "Bouvet Island" },
      { label: "Brazil" },
      { label: "British Indian Ocean Territory" },
      { label: "Brunei Darussalam" }
    ],
    allBrandNames: [
      "Intel",
      "AMD",
      "Asrock",
      "Asus",
      "Gigabyte",
      "Corsair",
      "Seasonic",
      "Samsung",
      "Sandisk",
      "Seagate"
    ],
    allSiteNames: ["StarTech", "Pickaboo", "Kiksha", "Google"]
  };

  /*
  componentDidMount() {
    axios.get('http://google.com/').then(res => {
      this.setState({
        searchResults=res.data
      });
    })
  }
  */

  FilterSiteNames = () => {
    const result = [];
    const map = new Map();
    for (const items of this.state.searchResults) {
      for (const item of items.website)
        if (!map.has(item.sitename)) {
          map.set(item.sitename, true); // set any value to Map
          result.push(item.sitename);
        }
    }
    return result;
  };

  GetMinMaxPrice = () => {
    const result = [];
    const map = new Map();
    for (const items of this.state.searchResults) {
      for (const item of items.website)
        if (!map.has(item.price)) {
          map.set(item.price, true); // set any value to Map
          result.push(item.price);
        }
    }
    return result.sort();
  };

  FilterResults = (price, brandName, siteName) => {
    let filterResults = [];
    //console.log(price);
    //console.log(brandName);
    //console.log(siteName);

    //filtering brand
    for (const items of this.state.searchResults) {
      for (const item of brandName) {
        if (items.brand === item) {
          if (!filterResults.includes(items)) filterResults.push(items);
        }
      }
    }

    //filtering sites
    let site = [];
    let fres = [];
    for (const a of filterResults) {
      site = [];
      for (const x of a.website) {
        for (const item of siteName) {
          if (x.sitename === item) {
            if (!site.includes(x)) site.push(x);
          }
        }
      }
      if (site.length > 0) {
        if (!fres.includes(a)) {
          a.website = site;
          fres.push(a);
        }
      }
    }
    filterResults = fres;

    //filtering price
    site = [];
    fres = [];
    for (const a of filterResults) {
      site = [];
      for (const x of a.website) {
        if (x.price >= price[0] && x.price <= price[1]) {
          if (!site.includes(x)) site.push(x);
        }
      }
      if (site.length > 0) {
        if (!fres.includes(a)) {
          a.website = site;
          fres.push(a);
        }
      }
    }
    filterResults = fres;

    this.setState({ filterResults });
    //console.log(this.state.searchResults);
    //console.log(filterResults);
  };

  render() {
    return (
      <React.Fragment>
        <AppBar />
        <AdvancedSearchBar
          category={this.state.category}
          allBrandNames={this.state.allBrandNames}
          allSiteNames={this.state.allSiteNames}
        />
        <Filter
          filterResults={this.FilterResults}
          filterPrice={this.GetMinMaxPrice()}
          filterBrandNames={[
            ...new Set(this.state.searchResults.map(x => x.brand))
          ]}
          filterSiteNames={this.FilterSiteNames()}
        />
        {this.state.filterResults.map(searchResult => (
          <SearchResult key={searchResult.id} searchResult={searchResult} />
        ))}
        <Footer />
      </React.Fragment>
    );
  }
}

export default SearchResults;
