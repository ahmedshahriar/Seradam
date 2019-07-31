import React, { Component } from "react";
import { BrowserRouter as Router } from "react-router-dom";
import BaseRouter from "./routes";

class Home extends Component {
  render() {
    return (
      <React.Fragment>
        <Router>
          <BaseRouter />
        </Router>
      </React.Fragment>
    );
  }
}

export default Home;
