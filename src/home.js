import React, { Component } from "react";
import AppBar from "./components/myAppBar";
import Footer from "./components/footer";
import SearchBar from "./components/searchBar";
import SearchResult from "./components/searchResult";

class Home extends Component {
  render() {
    return (
      <React.Fragment>
        <AppBar />
        <SearchBar />
        <SearchResult />
        <Footer />
      </React.Fragment>
    );
  }
}

export default Home;
