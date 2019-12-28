/*!

=========================================================
* Material Dashboard React - v1.7.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/material-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
import axios from "axios";
import Chartist from "chartist";
// nodejs library to set properties for components
import PropTypes from "prop-types";
// react plugin for creating charts
import ChartistGraph from "react-chartist";
// @material-ui/core
import withStyles from "@material-ui/core/styles/withStyles";
// @material-ui/icons
import Store from "@material-ui/icons/Store";
import Warning from "@material-ui/icons/Warning";
import DateRange from "@material-ui/icons/DateRange";
import LocalOffer from "@material-ui/icons/LocalOffer";
import Update from "@material-ui/icons/Update";
import AccessTime from "@material-ui/icons/AccessTime";
import Accessibility from "@material-ui/icons/Accessibility";
import BugReport from "@material-ui/icons/BugReport";
import Cloud from "@material-ui/icons/Cloud";
// core components
import GridItem from "../../components/Grid/GridItem.jsx";
import GridContainer from "../../components/Grid/GridContainer.jsx";
import Table from "../../components/Table/Table.jsx";
import Danger from "../../components/Typography/Danger.jsx";
import Card from "../../components/Card/Card.jsx";
import CardHeader from "../../components/Card/CardHeader.jsx";
import CardIcon from "../../components/Card/CardIcon.jsx";
import CardBody from "../../components/Card/CardBody.jsx";
import CardFooter from "../../components/Card/CardFooter.jsx";

import {
  dailySalesChart,
  emailsSubscriptionChart,
  completedTasksChart
} from "../../variables/charts.jsx";

import dashboardStyle from "../../assets/jss/material-dashboard-react/views/dashboardStyle.jsx";

class Dashboard extends React.Component {
  state = {
    value: 0,
    bpwu: [],
    swcu: [],
    usergraph: {},
    searchcountgraph: {},
    usergraphoptions: {},
    searchcountgraphoptions: {},
    isbpwu: false,
    isswcu: false,
    isusergraph: false,
    issearchcountgraph: false
  };

  componentDidMount() {
    //console.log(this.props);
    //brand products websites usercount
    var token = localStorage.getItem("token");
    var type = localStorage.getItem("type");
    if (type !== "admin") {
      this.props.history.push("/");
    }
    axios
      .get(
        "http://127.0.0.1:8000/products/brandproductswebsitesusercount/",
        {
          headers: {
            Authorization: `Token ${token}`
          }
        }
      )
      .then(res => {
        //console.log(res.data);
        this.setState({
          bpwu: res.data,
          isbpwu: true
        });
      })
      .catch(err => {
        console.log(err);
      });
    //user registration graph
    axios
      .get("http://127.0.0.1:8000/products/userregistrationgraph/", {
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then(res => {
        var result = [];
        var result1 = [];
        var maxNum = 0;
        var keys = Object.keys(res.data);
        keys.forEach(function(key) {
          result.push(res.data[key]);
        });
        maxNum = Math.max(...result);
        result1.push(result);
        //console.log(maxNum);
        this.setState({
          usergraph: {
            labels: keys,
            series: result1
          },
          usergraphoptions: {
            axisX: {
              showGrid: false
            },
            low: 0,
            high: maxNum + 5,
            chartPadding: {
              top: 0,
              right: 5,
              bottom: 0,
              left: 0
            }
          },
          isusergraph: true
        });
      })
      .catch(err => {
        console.log(err);
      });

    //search count per day
    axios
      .get("http://127.0.0.1:8000/products/searchcountperday/", {
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then(res => {
        var result = [];
        var result1 = [];
        var maxNum = 0;
        var keys = Object.keys(res.data);
        keys.forEach(function(key) {
          result.push(res.data[key]);
        });
        maxNum = Math.max(...result);
        result1.push(result);
        //console.log(res.data);
        this.setState({
          searchcountgraph: {
            labels: keys,
            series: result1
          },
          searchcountgraphoptions: {
            lineSmooth: Chartist.Interpolation.cardinal({
              tension: 0
            }),
            low: 0,
            high: maxNum + 5,
            chartPadding: {
              top: 0,
              right: 0,
              bottom: 0,
              left: 0
            }
          },
          issearchcountgraph: true
        });
      })
      .catch(err => {
        console.log(err);
      });

    //search wishlist count of user
    axios
      .get("http://127.0.0.1:8000/products/searchwishlistcountofuser/", {
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then(res => {
        var answer = res.data.map(el => Object.values(el));
        //console.log(answer);
        this.setState({
          swcu: answer,
          isswcu: true
        });
      })
      .catch(err => {
        console.log(err);
      });
  }

  handleChange = (event, value) => {
    this.setState({ value });
  };

  handleChangeIndex = index => {
    this.setState({ value: index });
  };
  render() {
    //console.log(this.state.isAdmin);
    // if (!this.state.isAdmin) {
    //   this.props.history.push("/");
    // }
    const { classes } = this.props;
    return (
      <div>
        {this.state.isbpwu ? (
          <GridContainer>
            <GridItem xs={12} sm={6} md={3}>
              <Card>
                <CardHeader color="rose" stats icon>
                  <CardIcon color="rose">
                    <Cloud />
                  </CardIcon>
                  <p className={classes.cardCategory}>Total Brands</p>
                  <h3 className={classes.cardTitle}>
                    {this.state.bpwu[0].total_brands}
                  </h3>
                </CardHeader>
                <CardFooter stats>
                  <div className={classes.stats}>
                    <Danger>
                      <Warning />
                    </Danger>
                    <a href="#pablo" onClick={e => e.preventDefault()}>
                      Everyday Brand New!
                    </a>
                  </div>
                </CardFooter>
              </Card>
            </GridItem>
            <GridItem xs={12} sm={6} md={3}>
              <Card>
                <CardHeader color="success" stats icon>
                  <CardIcon color="success">
                    <Store />
                  </CardIcon>
                  <p className={classes.cardCategory}>Total Products</p>
                  <h3 className={classes.cardTitle}>
                    {this.state.bpwu[0].total_products}
                  </h3>
                </CardHeader>
                <CardFooter stats>
                  <div className={classes.stats}>
                    <DateRange />
                    Increasing Day by Day!
                  </div>
                </CardFooter>
              </Card>
            </GridItem>
            <GridItem xs={12} sm={6} md={3}>
              <Card>
                <CardHeader color="warning" stats icon>
                  <CardIcon color="warning">
                    <BugReport />
                  </CardIcon>
                  <p className={classes.cardCategory}>Websites</p>
                  <h3 className={classes.cardTitle}>
                    {this.state.bpwu[0].total_websites}
                  </h3>
                </CardHeader>
                <CardFooter stats>
                  <div className={classes.stats}>
                    <LocalOffer />
                    Tracked from Database
                  </div>
                </CardFooter>
              </Card>
            </GridItem>
            <GridItem xs={12} sm={6} md={3}>
              <Card>
                <CardHeader color="info" stats icon>
                  <CardIcon color="info">
                    <Accessibility />
                  </CardIcon>
                  <p className={classes.cardCategory}>Users</p>
                  <h3 className={classes.cardTitle}>
                    {this.state.bpwu[0].total_users}
                  </h3>
                </CardHeader>
                <CardFooter stats>
                  <div className={classes.stats}>
                    <Update />
                    Just Updated
                  </div>
                </CardFooter>
              </Card>
            </GridItem>
          </GridContainer>
        ) : (
          ""
        )}

        <GridContainer>
          <GridItem xs={12} sm={12} md={12}>
            <Card chart>
              <CardHeader color="success">
                <ChartistGraph
                  className="ct-chart"
                  data={dailySalesChart.data}
                  type="Bar"
                  options={dailySalesChart.options}
                  listener={dailySalesChart.animation}
                />
              </CardHeader>
              <CardBody>
                <h4 className={classes.cardTitle}>Active Users</h4>
              </CardBody>
              <CardFooter chart>
                <div className={classes.stats}>
                  <AccessTime /> updated 4 minutes ago
                </div>
              </CardFooter>
            </Card>
          </GridItem>

          {this.state.isusergraph ? (
            <GridItem xs={12} sm={12} md={12}>
              <Card chart>
                <CardHeader color="warning">
                  <ChartistGraph
                    className="ct-chart"
                    data={this.state.usergraph}
                    type="Bar"
                    options={this.state.usergraphoptions}
                    responsiveOptions={
                      emailsSubscriptionChart.responsiveOptions
                    }
                    listener={emailsSubscriptionChart.animation}
                  />
                </CardHeader>
                <CardBody>
                  <h4 className={classes.cardTitle}>User Registration</h4>
                </CardBody>
                <CardFooter chart>
                  <div className={classes.stats}>
                    <AccessTime /> updated 5 minutes ago
                  </div>
                </CardFooter>
              </Card>
            </GridItem>
          ) : (
            ""
          )}

          {this.state.issearchcountgraph ? (
            <GridItem xs={12} sm={12} md={12}>
              <Card chart>
                <CardHeader color="danger">
                  <ChartistGraph
                    className="ct-chart"
                    data={this.state.searchcountgraph}
                    type="Bar"
                    options={this.state.searchcountgraphoptions}
                    listener={completedTasksChart.animation}
                  />
                </CardHeader>
                <CardBody>
                  <h4 className={classes.cardTitle}>Search Hits</h4>
                </CardBody>
                <CardFooter chart>
                  <div className={classes.stats}>
                    <AccessTime /> updated just now
                  </div>
                </CardFooter>
              </Card>
            </GridItem>
          ) : (
            ""
          )}
        </GridContainer>

        {this.state.isswcu ? (
          <GridContainer>
            <GridItem xs={12} sm={12} md={12}>
              <Card>
                <CardHeader color="warning">
                  <h4 className={classes.cardTitleWhite}>User Stats</h4>
                  <p className={classes.cardCategoryWhite}>Real Time Stats!</p>
                </CardHeader>
                <CardBody>
                  <Table
                    tableHeaderColor="warning"
                    tableHead={["Name", "Search Count", "WishList Count"]}
                    tableData={this.state.swcu}
                  />
                </CardBody>
              </Card>
            </GridItem>
          </GridContainer>
        ) : (
          ""
        )}
      </div>
    );
  }
}

Dashboard.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(dashboardStyle)(Dashboard);
