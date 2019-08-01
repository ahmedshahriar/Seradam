import React from "react";
import { Route } from "react-router-dom";
import Home from "./containers/home";
import SearchResults from "./containers/searchResults";

function BaseRouter(props) {
  //console.log(props);
  return (
    <div>
      <Route exact path="/" render={() => <Home {...props} />} />
      <Route exact path="/search" render={() => <SearchResults {...props} />} />
      <Route
        exact
        path="/:search/:category/:brand/:site"
        component={SearchResults}
      />
    </div>
  );
}

export default BaseRouter;
