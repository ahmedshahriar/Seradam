import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import Notification from "../components/notification";
import axios from "axios";

class WishLists extends Component {
  state = {
    notifications: [],
    appbarCount: []
  };

  componentDidMount() {
    var token = localStorage.getItem("token");
    axios
      .get("https://1666378e.ngrok.io/products/notification/", {
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then(res => {
        //console.log(res.data);
        this.setState({
          notifications: res.data
        });
      })
      .catch(err => {
        console.log(err);
      });

    if (token) {
      axios
        .get("https://1666378e.ngrok.io/products/notificationwishlistcount/", {
          headers: {
            Authorization: `Token ${token}`
          }
        })
        .then(res => {
          //console.log(res.data);
          this.setState({
            appbarCount: res.data
          });
        })
        .catch(err => {
          console.log(err);
        });
    }
  }

  render() {
    return (
      <React.Fragment>
        <AppBar {...this.props} appbar={this.state.appbarCount} />
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
