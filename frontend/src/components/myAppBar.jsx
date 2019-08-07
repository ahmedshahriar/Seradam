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
import ProfileMenu from "./profileMenu";
import LockIcon from "@material-ui/icons/Lock";
import RegIcon from "@material-ui/icons/AccessibilityNew";
import NotificationIcon from "@material-ui/icons/Notifications";
import WishListIcon from "@material-ui/icons/EventNote";
import LogoutIcon from "@material-ui/icons/ExitToApp";

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
              <ProfileMenu />
              <Link
                href="/notification"
                target="_blank"
                rel="noreferrer"
                color="inherit"
              >
                <Button aria-describedby="wishlist" color="inherit">
                  <NotificationIcon /> Notification
                </Button>
              </Link>
              <Link
                href="/wishlist"
                target="_blank"
                rel="noreferrer"
                color="inherit"
              >
                <Button aria-describedby="wishlist" color="inherit">
                  <WishListIcon /> WishList
                </Button>
              </Link>
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
                  <SignIn />
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
