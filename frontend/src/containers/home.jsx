import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import SearchBar from "../components/searchBar";

class HomePage extends Component {
  render() {
    //console.log(this.props);
    return (
      <React.Fragment>
        <AppBar {...this.props} />
        <SearchBar />
        <Footer />
      </React.Fragment>
    );
  }
}

export default HomePage;
