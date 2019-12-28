import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import AdvancedSearchBar from "../components/advancedSearchBar";
import SearchResult from "../components/searchResult";
import Filter from "../components/filter";
import Typography from "@material-ui/core/Typography";
import CircularProgress from "@material-ui/core/CircularProgress";
import axios from "axios";

class SearchResults extends Component {
  state = {
    searchResults: [],
    filterResults: [],
    category: [{ label: "Laptop" }],
    allBrandNames: [],
    allSiteNames: ["ryanscomputers.com", "startech.com.bd"],
    resultFound: true,
    wishList: [],
    appbarCount: []
  };

  componentDidMount() {
    var key = this.getQueryVariable("search");
    var brand = this.getQueryVariable("brand");
    var site = this.getQueryVariable("site");
    var category = this.getQueryVariable("category");
    var token = localStorage.getItem("token");
    //console.log(brand);
    if (token) {
      axios
        .get("http://127.0.0.1:8000/products/notificationwishlistcount/", {
          headers: {
            Authorization: `Token ${token}`
          }
        })
        .then(res => {
          //console.log(res.data);
          this.setState({
            appbarCount: res.data
          });
        })
        .catch(err => {
          console.log(err);
        });
    }

    if (token) {
      axios
        .get("http://127.0.0.1:8000/wishlist/", {
          headers: {
            Authorization: `Token ${token}`
          }
        })
        .then(res => {
          this.setState({
            wishList: res.data
          });
        });
    }

    if (token) {
      axios
        .get(
          `http://127.0.0.1:8000/products/mapping/?key=${key}&brand=${brand}&category=${category}&site=${site}`,
          {
            headers: {
              Authorization: `Token ${token}`
            }
          }
        )
        .then(res => {
          for (var i = 0; i < res.data.length; i++) {
            var d = "";
            var p = res.data[i].description;

            for (var l = 0; l < p.length; l++) {
              if (p[l] !== "'") {
                //console.log(i);
                d += p[l];
              }
            }

            var des_lenght = d.length;
            d = d.substr(1, des_lenght - 2);

            d = d.split(",").map(function(item) {
              return item.trim();
            });

            var storage = {};
            var temp = res.data[i].storage;
            var last = 0;

            while (temp.indexOf("'", last) !== -1) {
              last = temp.indexOf("'", last) + 1;
              var next = temp.indexOf("'", last);
              var type = temp.substr(last, next - last);
              last = next + 1;

              last = temp.indexOf("'", last) + 1;
              next = temp.indexOf("'", last);
              var size = temp.substr(last, next - last);
              last = next + 1;
              //console.log(type + " : "+size);
              storage[type] = size;
            }
            //console.log(storage);

            var websites = [];
            var last_found = 0;
            var s = res.data[i].websites;

            var website_len = "website_name".length;
            var price_len = "price".length;
            var product_link_len = "product_link".length;
            var status_len = "status".length;
            var img_link_len = "img_link".length;

            while (s.indexOf("OrderedDict", last_found) !== -1) {
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
              var price_size =
                s.indexOf(")", price_start_pos) - price_start_pos;
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
                website_name: website_name,
                price: price,
                img_link: img_link,
                product_link: product_link,
                status: status
              };
              websites.push(result);
            }
            res.data[i].websites = websites;
            res.data[i].description = d;
            res.data[i].storage = storage;
          }
          this.setState({
            searchResults: res.data,
            filterResults: res.data
          });
          if (this.state.searchResults.length > 0) {
            this.setState({
              resultFound: true
            });
          } else {
            this.setState({
              resultFound: false
            });
          }
          //console.log(this.state.searchResults);
        })
        .catch(err => {
          console.log(err);
          this.setState({
            resultFound: false
          });
        });
    } else {
      axios
        .get(
          `http://127.0.0.1:8000/products/mapping/?key=${key}&brand=${brand}&category=${category}&site=${site}`
        )
        .then(res => {
          for (var i = 0; i < res.data.length; i++) {
            var d = "";
            var p = res.data[i].description;

            for (var l = 0; l < p.length; l++) {
              if (p[l] !== "'") {
                //console.log(i);
                d += p[l];
              }
            }

            var des_lenght = d.length;
            d = d.substr(1, des_lenght - 2);

            d = d.split(",").map(function(item) {
              return item.trim();
            });

            var storage = {};
            var temp = res.data[i].storage;
            var last = 0;

            while (temp.indexOf("'", last) !== -1) {
              last = temp.indexOf("'", last) + 1;
              var next = temp.indexOf("'", last);
              var type = temp.substr(last, next - last);
              last = next + 1;

              last = temp.indexOf("'", last) + 1;
              next = temp.indexOf("'", last);
              var size = temp.substr(last, next - last);
              last = next + 1;
              //console.log(type + " : "+size);
              storage[type] = size;
            }
            //console.log(storage);

            var websites = [];
            var last_found = 0;
            var s = res.data[i].websites;

            var website_len = "website_name".length;
            var price_len = "price".length;
            var product_link_len = "product_link".length;
            var status_len = "status".length;
            var img_link_len = "img_link".length;

            while (s.indexOf("OrderedDict", last_found) !== -1) {
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
              var price_size =
                s.indexOf(")", price_start_pos) - price_start_pos;
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
                website_name: website_name,
                price: price,
                img_link: img_link,
                product_link: product_link,
                status: status
              };
              websites.push(result);
            }
            res.data[i].websites = websites;
            res.data[i].description = d;
            res.data[i].storage = storage;
          }
          this.setState({
            searchResults: res.data,
            filterResults: res.data
          });
          if (this.state.searchResults.length > 0) {
            this.setState({
              resultFound: true
            });
          } else {
            this.setState({
              resultFound: false
            });
          }
          //console.log(this.state.searchResults);
        })
        .catch(err => {
          console.log(err);
          this.setState({
            resultFound: false
          });
        });
    }

    axios
      .get("http://127.0.0.1:8000/products/brand/")
      .then(res => {
        this.setState({
          allBrandNames: res.data
        });
      })
      .catch(err => {
        console.log(err);
      });
  }

  getQueryVariable = variable => {
    var query = window.location.search.substring(1);
    //console.log(query); //"app=article&act=news_content&aid=160990"
    var vars = query.split("&");
    //console.log(vars); //[ 'app=article', 'act=news_content', 'aid=160990' ]
    for (var i = 0; i < vars.length; i++) {
      var pair = vars[i].split("=");
      //console.log(pair); //[ 'app', 'article' ][ 'act', 'news_content' ][ 'aid', '160990' ]
      if (pair[0] === variable) {
        return pair[1];
      }
    }
    return false;
  };

  FilterSiteNames = () => {
    const result = [];
    const map = new Map();
    for (const items of this.state.searchResults) {
      for (const item of items.websites)
        if (!map.has(item.website_name)) {
          map.set(item.website_name, true); // set any value to Map
          result.push(item.website_name);
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
    var site = [];
    var fres = [];
    //console.log(price);
    //console.log(brandName);
    //console.log(siteName);

    //filtering brand
    if (brandName.length > 0) {
      for (const items of this.state.searchResults) {
        for (const item of brandName) {
          if (items.brand === item) {
            if (!newResults.includes(items)) newResults.push(items);
          }
        }
      }
    } else {
      newResults = this.state.searchResults;
    }

    //filtering sites

    if (siteName.length > 0) {
      for (const a of newResults) {
        site = [];
        for (const x of a.websites) {
          for (const item of siteName) {
            if (x.website_name === item) {
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
      newResults = fres;
    } else {
      newResults = this.state.searchResults;
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

    //filtering price
    site = [];
    fres = [];
    if (price[0] !== undefined && price[1] !== undefined) {
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
    }

    this.setState({ filterResults: newResults });
    //console.log(this.state.searchResults);
    //console.log(filterResults);
  };

  render() {
    return (
      <React.Fragment>
        <AppBar {...this.props} appbar={this.state.appbarCount} />
        <AdvancedSearchBar
          category={this.state.category}
          allBrandNames={this.state.allBrandNames}
          allSiteNames={this.state.allSiteNames}
        />
        {this.state.searchResults.length ? (
          <React.Fragment>
            <Filter
              filterResults={this.FilterResults}
              filterPrice={this.GetMinMaxPrice()}
              filterBrandNames={[
                ...new Set(this.state.searchResults.map(x => x.brand))
              ]}
              filterSiteNames={this.FilterSiteNames()}
            />
            {this.state.filterResults.map(searchResult => (
              <SearchResult
                key={searchResult.id}
                searchResult={searchResult}
                wishList={this.state.wishList}
                {...this.props}
              />
            ))}
          </React.Fragment>
        ) : (
          <Typography align="center">
            {this.state.resultFound ? (
              <CircularProgress disableShrink />
            ) : (
              <Typography align="center">"No Result Found"</Typography>
            )}
          </Typography>
        )}
        <Footer />
      </React.Fragment>
    );
  }
}

export default SearchResults;
