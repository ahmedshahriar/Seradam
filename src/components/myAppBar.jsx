import React from "react";
import SignIn from "./signIn";
import SignUp from "./signUp";
import Popover from "@material-ui/core/Popover";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1
  },
  title: {
    flexGrow: 1
  }
}));

export default function MyAppBar() {
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
          <Button aria-describedby={id} color="inherit" onClick={handleClick}>
            Login
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
          <Button aria-describedby={id1} color="inherit" onClick={handleClick1}>
            Sign Up
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
        </Toolbar>
      </AppBar>
    </div>
  );
}
