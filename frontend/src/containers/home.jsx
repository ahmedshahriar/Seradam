import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import SearchBar from "../components/searchBar";
import axios from "axios";

class HomePage extends Component {
  state = {
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
  }

  render() {
    //console.log(this.props);
    return (
      <React.Fragment>
        <AppBar {...this.props} appbar={this.state.appbarCount} />
        <SearchBar />
        <Footer />
      </React.Fragment>
    );
  }
}

export default HomePage;
