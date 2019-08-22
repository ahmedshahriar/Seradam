import React from "react";
import { connect } from "react-redux";
import * as actions from "../store/actions/auth";
import { withRouter } from "react-router-dom";
import SignIn from "./signIn";
import SignUp from "./signUp";
import Popover from "@material-ui/core/Popover";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import Link from "@material-ui/core/Link";
//import ProfileMenu from "./profileMenu";
import LockIcon from "@material-ui/icons/Lock";
import RegIcon from "@material-ui/icons/AccessibilityNew";
import NotificationIcon from "@material-ui/icons/Notifications";
import WishListIcon from "@material-ui/icons/EventNote";
import LogoutIcon from "@material-ui/icons/ExitToApp";
import Badge from "@material-ui/core/Badge";

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1
  },
  title: {
    flexGrow: 1
  }
}));

function MyAppBar(props) {
  //console.log(props);
  // if (props.appbar && props.appbar.length > 0) {
  //   console.log(props.appbar);
  // }

  const type = localStorage.getItem("type");
  //console.log(type);

  const classes = useStyles();

  const [anchorEl, setAnchorEl] = React.useState(null);
  const [anchorEl1, setAnchorEl1] = React.useState(null);

  function handleClick(event) {
    setAnchorEl(event.currentTarget);
  }

  function handleClose() {
    setAnchorEl(null);
  }
  function handleClick1(event) {
    setAnchorEl1(event.currentTarget);
  }

  function handleClose1() {
    setAnchorEl1(null);
  }

  const open = Boolean(anchorEl);
  const id = open ? "simple-popover" : undefined;

  const open1 = Boolean(anchorEl1);
  const id1 = open1 ? "simple-popover" : undefined;

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            SeraDam.Com
          </Typography>
          {props.isAuthenticated ? (
            <React.Fragment>
              {type === "normaluser" ? (
                <React.Fragment>
                  {/* <ProfileMenu /> */}
                  <Link
                    href="/notification"
                    target="_blank"
                    rel="noreferrer"
                    color="inherit"
                  >
                    {props.appbar && props.appbar.length > 0 ? (
                      <Badge
                        color="secondary"
                        badgeContent={props.appbar[0].notification_count}
                        className={classes.margin}
                      >
                        <Button aria-describedby="wishlist" color="inherit">
                          <NotificationIcon /> Notification
                        </Button>
                      </Badge>
                    ) : (
                      ""
                    )}
                  </Link>
                  <Link
                    href="/wishlist"
                    target="_blank"
                    rel="noreferrer"
                    color="inherit"
                  >
                    {props.appbar && props.appbar.length > 0 ? (
                      <Badge
                        color="secondary"
                        badgeContent={props.appbar[0].wishlist_count}
                        className={classes.margin}
                      >
                        <Button aria-describedby="wishlist" color="inherit">
                          <WishListIcon /> WishList
                        </Button>
                      </Badge>
                    ) : (
                      ""
                    )}
                  </Link>
                </React.Fragment>
              ) : (
                <Link
                  href="/admin"
                  target="_blank"
                  rel="noreferrer"
                  color="inherit"
                >
                  <Button aria-describedby="wishlist" color="inherit">
                    Admin Panel
                  </Button>
                </Link>
              )}

              <Button
                aria-describedby="logout"
                color="inherit"
                onClick={props.logout}
              >
                <LogoutIcon /> Logout
              </Button>
            </React.Fragment>
          ) : (
            <React.Fragment>
              <Button
                aria-describedby={id}
                color="inherit"
                onClick={handleClick}
              >
                <LockIcon /> Login
              </Button>
              <Popover
                id={id}
                open={open}
                anchorEl={anchorEl}
                onClose={handleClose}
                anchorOrigin={{
                  vertical: "bottom",
                  horizontal: "center"
                }}
                transformOrigin={{
                  vertical: "top",
                  horizontal: "center"
                }}
              >
                <Typography className={classes.typography}>
                  <SignIn history={props.history} />
                </Typography>
              </Popover>
              <Button
                aria-describedby={id1}
                color="inherit"
                onClick={handleClick1}
              >
                <RegIcon /> Sign Up
              </Button>
              <Popover
                id={id1}
                open={open1}
                anchorEl={anchorEl1}
                onClose={handleClose1}
                anchorOrigin={{
                  vertical: "bottom",
                  horizontal: "center"
                }}
                transformOrigin={{
                  vertical: "top",
                  horizontal: "center"
                }}
              >
                <Typography className={classes.typography}>
                  <SignUp />
                </Typography>
              </Popover>
            </React.Fragment>
          )}
        </Toolbar>
      </AppBar>
    </div>
  );
}

const mapDispatchToProps = dispatch => {
  return {
    logout: () => dispatch(actions.logout())
  };
};

export default withRouter(
  connect(
    null,
    mapDispatchToProps
  )(MyAppBar)
);
