import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import Snackbar from "@material-ui/core/Snackbar";
import IconButton from "@material-ui/core/IconButton";
import CloseIcon from "@material-ui/icons/Close";
import axios from "axios";

const useStyles = makeStyles(theme => ({
  close: {
    padding: theme.spacing(0.5)
  }
}));

export default function SimpleSnackbar(props) {
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  function handleClick() {
    //console.log(props);
    //console.log(localStorage.getItem("token"));
    axios
      .post("http://365b70d4.ngrok.io/wishlist/", {
        website_name: "Ryan",
        product_link: "http://localhost:3000/",
        price: 6000,
        user: 2
      })
      .then(res => {
        console.log(res.data);
      })
      .catch(err => {
        console.log(err);
      });
    setOpen(true);
  }

  function handleClose(event, reason) {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  }

  return (
    <div>
      <Button onClick={handleClick}>Add to Wishlist</Button>
      <Snackbar
        anchorOrigin={{
          vertical: "bottom",
          horizontal: "left"
        }}
        open={open}
        autoHideDuration={3000}
        onClose={handleClose}
        ContentProps={{
          "aria-describedby": "message-id"
        }}
        message={<span id="message-id">Product Added to Wishlist!</span>}
        action={[
          <Button
            key="undo"
            color="secondary"
            size="small"
            onClick={handleClose}
          >
            UNDO
          </Button>,
          <IconButton
            key="close"
            aria-label="close"
            color="inherit"
            className={classes.close}
            onClick={handleClose}
          >
            <CloseIcon />
          </IconButton>
        ]}
      />
    </div>
  );
}
