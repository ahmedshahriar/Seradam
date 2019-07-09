import React, { Component } from "react";
import SearchResult from "./searchResult";

class SearchResults extends Component {
  state = {
    searchResults: [
      {
        id: 1,
        imageUrl: "https://picsum.photos/200",
        name: "Ram 8GB",
        desc: "DDR5 5000 RPM",
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
    ]
  };
  render() {
    return (
      <div>
        {this.state.searchResults.map(searchResult => (
          <SearchResult key={searchResult.id} searchResult={searchResult} />
        ))}
      </div>
    );
  }
}

export default SearchResults;
