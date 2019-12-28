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
  //console.log(props.wishList);
  var wish = false;
  if (
    props.wishList.some(
      e => e.product_title === props.searchResult.product_title
    )
  ) {
    wish = false;
  } else {
    wish = true;
  }
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  function handleClick() {
    var token = localStorage.getItem("token");
    //console.log(`Token ${token}`);
    //console.log(props);
    //console.log(localStorage.getItem("token"));
    axios
      .post("http://127.0.0.1:8000/wishlist/", props.searchResult, {
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then(res => {
        console.log(res);
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
      {wish ? (
        <React.Fragment>
          <Button
            size="small"
            variant="contained"
            color="secondary"
            fullWidth
            onClick={handleClick}
          >
            Add to Wishlist
          </Button>
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
        </React.Fragment>
      ) : (
        "Added To WishList!"
      )}
    </div>
  );
}
