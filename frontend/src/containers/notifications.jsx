import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import Notification from "../components/notification";
import axios from "axios";
//import { Redirect } from "react-router-dom";

class WishLists extends Component {
  state = {
    notifications: [],
    appbarCount: []
  };

  componentDidMount() {
    //console.log(this.props);
    var token = localStorage.getItem("token");
    var type = localStorage.getItem("type");
    if (type !== "normaluser") {
      //console.log(this.props.history);
      //this.props.history("push", "/");
    }
    axios
      .get("http://127.0.0.1:8000/products/notification/", {
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
        .get("http://127.0.0.1:8000/products/notificationwishlistcount/", {
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
