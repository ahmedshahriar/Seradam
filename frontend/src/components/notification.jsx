import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Link from "@material-ui/core/Link";
import Paper from "@material-ui/core/Paper";
import Container from "@material-ui/core/Container";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(1),
    width: "100%",
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper
  }
}));

export default function Notification(props) {
  //console.log(props.notification.seen);
  const classes = useStyles();

  return (
    <React.Fragment>
      <Container component="main">
        <div className={classes.root}>
          <Paper className={classes.root}>
            {props.notification.seen ? (
              <React.Fragment>
                <Typography variant="h5" component="h3">
                  <Link
                    href={props.notification.product_link}
                    target="_blank"
                    rel="noreferrer"
                    color="inherit"
                  >
                    {props.notification.product_title}
                  </Link>
                </Typography>
                <Typography component="p">
                  Website Name: <b>{props.notification.website_name}</b> Old
                  Price: <b>{props.notification.old_price}</b> New price:{" "}
                  <b>{props.notification.new_price}</b>{" "}
                </Typography>
              </React.Fragment>
            ) : (
              <React.Fragment>
                <Typography variant="h5" component="h3" color="Secondary">
                  <Link
                    href={props.notification.product_link}
                    target="_blank"
                    rel="noreferrer"
                    color="inherit"
                  >
                    {props.notification.product_title}
                  </Link>
                </Typography>
                <Typography component="p">
                  Website Name: <b>{props.notification.website_name}</b> Old
                  Price: <b>{props.notification.old_price}</b> New price:{" "}
                  <b>{props.notification.new_price}</b>{" "}
                </Typography>
              </React.Fragment>
            )}
          </Paper>
        </div>
      </Container>
    </React.Fragment>
  );
}
