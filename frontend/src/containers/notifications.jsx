import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import Notification from "../components/notification";
import axios from "axios";

class WishLists extends Component {
  state = {
    notifications: []
  };

  componentDidMount() {
    var token = localStorage.getItem("token");
    axios
      .get("https://d64e77b6.ngrok.io/products/notification/", {
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then(res => {
        this.setState({
          notifications: res.data
        });
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
      <React.Fragment>
        <AppBar {...this.props} />
        {this.state.notifications.map(notification => (
          <Notification
            key={notification.id}
            notification={notification}
            {...this.props}
          />
        ))}
        <Footer />
      </React.Fragment>
    );
  }
}

export default WishLists;
