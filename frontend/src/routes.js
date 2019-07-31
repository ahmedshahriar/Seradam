import React from "react";
import { Route } from "react-router-dom";
import Home from "./containers/home";
import SearchResults from "./containers/searchResults";

const BaseRouter = () => (
  <div>
    <Route exact path="/" component={Home} />
    <Route exact path="/search" component={SearchResults} />
    <Route
      exact
      path="/:search/:category/:brand/:site"
      component={SearchResults}
    />
  </div>
);

export default BaseRouter;
