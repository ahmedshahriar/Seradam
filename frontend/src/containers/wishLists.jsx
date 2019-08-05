import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import SearchResult from "../components/wishList";
import axios from "axios";

class WishLists extends Component {
  state = {
    searchResults: []
  };

  componentDidMount() {
    axios
      .get("https://ab1307df.ngrok.io/wishlist/")
      .then(res => {
        console.log(res.data);
      })
      .catch(err => {
        console.log(err);
      });
    // axios.get("https://f570cf48.ngrok.io/wishlist").then(res => {
    // for (var i = 0; i < res.data.length; i++) {
    //   var s = res.data[i].websites;
    //   var websites = [];
    //   var last_found = 0;

    //   var website_len = "website_name".length;
    //   var price_len = "price".length;
    //   var product_link_len = "product_link".length;
    //   var status_len = "status".length;
    //   var img_link_len = "img_link".length;

    //   while (s.indexOf("OrderedDict", last_found) != -1) {
    //     last_found = s.indexOf("OrderedDict", last_found);

    //     var website_name_start_pos =
    //       s.indexOf("website_name", last_found) + website_len + 4;
    //     var website_name_size =
    //       s.indexOf("'", website_name_start_pos) - website_name_start_pos;
    //     var website_name = s.substr(
    //       website_name_start_pos,
    //       website_name_size
    //     );
    //     last_found = website_name_size + website_name_start_pos;

    //     var price_start_pos =
    //       s.indexOf("price", last_found) + price_len + 3;
    //     var price_size = s.indexOf(")", price_start_pos) - price_start_pos;
    //     var price_str = "0" + s.substr(price_start_pos, price_size); //adding 0, so that it convert to 0 if any problem occurs
    //     var price = parseInt(price_str);
    //     last_found = price_size + price_start_pos;

    //     var product_link_start_pos =
    //       s.indexOf("product_link", last_found) + product_link_len + 4;
    //     var product_link_size =
    //       s.indexOf("'", product_link_start_pos) - product_link_start_pos;
    //     var product_link = s.substr(
    //       product_link_start_pos,
    //       product_link_size
    //     );
    //     last_found = product_link_size + product_link_start_pos;

    //     var status_start_pos =
    //       s.indexOf("status", last_found) + status_len + 4;
    //     var status_size =
    //       s.indexOf("'", status_start_pos) - status_start_pos;
    //     var status = s.substr(status_start_pos, status_size);
    //     last_found = status_size + status_start_pos;

    //     var img_link_start_pos =
    //       s.indexOf("img_link", last_found) + img_link_len + 4;
    //     var img_link_size =
    //       s.indexOf("'", img_link_start_pos) - img_link_start_pos;
    //     var img_link = s.substr(img_link_start_pos, img_link_size);
    //     last_found = img_link_size + img_link_start_pos;

    //     var result = {
    //       sitename: website_name,
    //       price: price,
    //       img_link: img_link,
    //       p_link: product_link,
    //       status: status
    //     };
    //     websites.push(result);
    //   }
    //   res.data[i].websites = websites;
    // }
    // this.setState({
    //   searchResults: res.data
    // });
    // });
  }

  render() {
    return (
      <React.Fragment>
        <AppBar {...this.props} />
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
