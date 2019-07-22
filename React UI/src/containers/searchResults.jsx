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
        imageUrl: "https://picsum.photos/200",
        name: "Ram 8GB",
        desc:
          "DDR5 5000 RPM hi uiyrg7wyrstiyw suityeit tei7ty euityt a4ity ae8ty9",
        site1name: "StarTech.Com.Bd",
        site1price: 450,
        site1url: "https://google.com/"
      },
      {
        id: 2,
        imageUrl: "https://picsum.photos/200",
        name: "Ram 16GB",
        desc: "DDR5 5200 RPM",
        site1name: "Pickaboo.com",
        site1price: 550,
        site1url: "https://google.com/",
        site2name: "StarTech.Com.Bd",
        site2price: 570,
        site2url: "https://google.com/"
      },
      {
        id: 3,
        imageUrl: "https://picsum.photos/200",
        name: "Ram 32GB",
        desc: "DDR5 5400 RPM",
        site1name: "Pickaboo.com",
        site1price: 600,
        site1url: "https://google.com/",
        site2name: "StarTech.Com.Bd",
        site2price: 610,
        site2url: "https://google.com/",
        site3name: "Kiksha.com",
        site3price: 620,
        site3url: "https://google.com/"
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
    filterBrandNames: ["Intel", "AMD", "Asrock", "Asus"],
    filterSiteNames: ["StarTech", "Pickaboo", "Google"],
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
  componentDidMount(){
    axios.get('http://google.com/').then(res => {
      this.setState({
        searchResults=res.data
      });
    })
  }
  */
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
          filterBrandNames={this.state.filterBrandNames}
          filterSiteNames={this.state.filterSiteNames}
        />
        {this.state.searchResults.map(searchResult => (
          <SearchResult key={searchResult.id} searchResult={searchResult} />
        ))}
        <Footer />
      </React.Fragment>
    );
  }
}

export default SearchResults;
