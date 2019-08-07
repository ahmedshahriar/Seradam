import React, { Component } from "react";
import AppBar from "../components/myAppBar";
import Footer from "../components/footer";
import Notification from "../components/notification";
import axios from "axios";

class WishLists extends Component {
  state = {
    notifications: [
      {
        product_title: "Hp Probook G5",
        website_name: "ryanscomputers.com",
        product_link: "http://google.com",
        old_price: 56500,
        new_price: 55000,
        time: "2019-8-7 9:26:7"
      },
      {
        product_title: "Hp Probook G4",
        website_name: "ryanscomputers.com",
        product_link: "http://google.com",
        old_price: 56500,
        new_price: 55000,
        time: "2019-8-7 9:26:7"
      }
    ]
  };

  componentDidMount() {
    // var token = localStorage.getItem("token");
    // axios
    //   .get("http://127.0.0.1:8000/notification/", {
    //     headers: {
    //       Authorization: `Token ${token}`
    //     }
    //   })
    //   .then(res => {
    //     this.setState({
    //       notifications: res.data
    //     });
    //   })
    //   .catch(err => {
    //     console.log(err);
    //   });
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
