import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import SearchResult from "../components/wishList";
import axios from "axios";

class WishLists extends Component {
  state = {
    searchResults: [],
    appbarCount: []
  };

  componentDidMount() {
    var token = localStorage.getItem("token");

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

    axios
      .get("http://127.0.0.1:8000/wishlist/", {
        headers: {
          Authorization: `Token ${token}`
        }
      })
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
          searchResults: res.data
        });
        //console.log(this.state.searchResults);
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
      <React.Fragment>
        <AppBar {...this.props} appbar={this.state.appbarCount} />
        {this.state.searchResults.map(searchResult => (
          <SearchResult
            key={searchResult.id}
            searchResult={searchResult}
            {...this.props}
          />
        ))}
        <Footer />
      </React.Fragment>
    );
  }
}

export default WishLists;
