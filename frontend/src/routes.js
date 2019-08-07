import React from "react";
import { Route } from "react-router-dom";
import Home from "./containers/home";
import SearchResults from "./containers/searchResults";
import WishList from "./containers/wishLists";
import Notifications from "./containers/notifications";

import Admin from "./layouts/Admin";

import "./assets/css/material-dashboard-react.css?v=1.7.0";

function BaseRouter(props) {
  //console.log(props);
  return (
    <div>
      <Route path="/admin" component={Admin} />
      <Route exact path="/" render={() => <Home {...props} />} />
      <Route exact path="/search" render={() => <SearchResults {...props} />} />
      <Route exact path="/wishlist" render={() => <WishList {...props} />} />
      <Route
        exact
        path="/notification"
        render={() => <Notifications {...props} />}
      />
      <Route
        exact
        path="/search/?search=:search&category=:category"
        component={SearchResults}
      />
    </div>
  );
}

export default BaseRouter;
