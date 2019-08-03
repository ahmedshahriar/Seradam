import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import AdvancedSearchBar from "../components/advancedSearchBar";
import SearchResult from "../components/searchResult";
import Filter from "../components/filter";
import axios from "axios";

class SearchResults extends Component {
  state = {
    searchResults: [],
    filterResults: [],
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

  componentDidMount() {
    axios
      .get(
        "http://2288a47b.ngrok.io/products/mapping/?brand=Acer&graphics_memory=4GB"
      )
      .then(res => {
        for (var i = 0; i < res.data.length; i++) {
          var s = res.data[i].websites;
          var websites = [];
          var last_found = 0;

          var website_len = "website_name".length;
          var price_len = "price".length;
          var product_link_len = "product_link".length;
          var status_len = "status".length;
          var img_link_len = "img_link".length;

          while (s.indexOf("OrderedDict", last_found) != -1) {
            last_found = s.indexOf("OrderedDict", last_found);

            var website_name_start_pos =
              s.indexOf("website_name", last_found) + website_len + 4;
            var website_name_size =
              s.indexOf("'", website_name_start_pos) - website_name_start_pos;
            var website_name = s.substr(
              website_name_start_pos,
              website_name_size
            );
            last_found = website_name_size + website_name_start_pos;

            var price_start_pos =
              s.indexOf("price", last_found) + price_len + 3;
            var price_size = s.indexOf(")", price_start_pos) - price_start_pos;
            var price_str = "0" + s.substr(price_start_pos, price_size); //adding 0, so that it convert to 0 if any problem occurs
            var price = parseInt(price_str);
            last_found = price_size + price_start_pos;

            var product_link_start_pos =
              s.indexOf("product_link", last_found) + product_link_len + 4;
            var product_link_size =
              s.indexOf("'", product_link_start_pos) - product_link_start_pos;
            var product_link = s.substr(
              product_link_start_pos,
              product_link_size
            );
            last_found = product_link_size + product_link_start_pos;

            var status_start_pos =
              s.indexOf("status", last_found) + status_len + 4;
            var status_size =
              s.indexOf("'", status_start_pos) - status_start_pos;
            var status = s.substr(status_start_pos, status_size);
            last_found = status_size + status_start_pos;

            var img_link_start_pos =
              s.indexOf("img_link", last_found) + img_link_len + 4;
            var img_link_size =
              s.indexOf("'", img_link_start_pos) - img_link_start_pos;
            var img_link = s.substr(img_link_start_pos, img_link_size);
            last_found = img_link_size + img_link_start_pos;

            var result = {
              sitename: website_name,
              price: price,
              img_link: img_link,
              p_link: product_link,
              status: status
            };
            websites.push(result);
          }
          res.data[i].websites = websites;
        }
        this.setState({
          searchResults: res.data,
          filterResults: res.data
        });
      });
  }

  FilterSiteNames = () => {
    const result = [];
    const map = new Map();
    for (const items of this.state.searchResults) {
      for (const item of items.websites)
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
      for (const item of items.websites)
        if (!map.has(item.price)) {
          map.set(item.price, true); // set any value to Map
          result.push(item.price);
        }
    }
    return result.sort();
  };

  FilterResults = (price, brandName, siteName) => {
    var newResults = [];
    console.log(price);
    console.log(brandName);
    console.log(siteName);

    //filtering brand
    for (const items of this.state.searchResults) {
      for (const item of brandName) {
        if (items.brand === item) {
          if (!newResults.includes(items)) newResults.push(items);
        }
      }
    }

    //filtering sites
    var site = [];
    var fres = [];
    for (const a of newResults) {
      site = [];
      for (const x of a.websites) {
        for (const item of siteName) {
          if (x.sitename === item) {
            if (!site.includes(x)) site.push(x);
          }
        }
      }
      if (site.length > 0) {
        if (!fres.includes(a)) {
          a.websites = site;
          fres.push(a);
        }
      }
    }

    // for (var i = 0; i < newResults.length; i++) {
    //   site = [];
    //   for (var j = 0; j < newResults[i].websites.length; i++) {
    //     for (var k = 0; k < siteName.length; k++) {
    //       if (newResults[i].websites[j].sitename == siteName[k]) {
    //         if (!site.includes(newResults[i].websites[j]))
    //           site.push(newResults[i].websites[j]);
    //       }
    //     }
    //   }
    //   if (site.length) {
    //     newResults[i].websites = site;
    //   }
    // }
    newResults = fres;

    //filtering price
    site = [];
    fres = [];
    for (const a of newResults) {
      site = [];
      for (const x of a.websites) {
        if (x.price >= price[0] && x.price <= price[1]) {
          if (!site.includes(x)) site.push(x);
        }
      }
      if (site.length > 0) {
        if (!fres.includes(a)) {
          a.websites = site;
          fres.push(a);
        }
      }
    }
    newResults = fres;

    this.setState({ filterResults: newResults });
    //console.log(this.state.searchResults);
    //console.log(filterResults);
  };

  render() {
    //console.log(this.state.searchResults);
    return (
      <React.Fragment>
        <AppBar {...this.props} />
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
