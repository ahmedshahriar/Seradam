import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import SearchBar from "../components/searchBar";

class HomePage extends Component {
  render() {
    return (
      <React.Fragment>
        <AppBar />
        <SearchBar />
        <Footer />
      </React.Fragment>
    );
  }
}

export default HomePage;
