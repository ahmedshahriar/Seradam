import React, { Component } from "react";
import AppBar from "./components/myAppBar";
import Footer from "./components/footer";
import SearchBar from "./components/searchBar";
import SearchResults from "./components/searchResults";

class Home extends Component {
  render() {
    return (
      <React.Fragment>
        <AppBar />
        <SearchBar />
        <SearchResults />
        <Footer />
      </React.Fragment>
    );
  }
}

export default Home;
