import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import ButtonBase from "@material-ui/core/ButtonBase";
import Button from "@material-ui/core/Button";
import Link from "@material-ui/core/Link";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import Container from "@material-ui/core/Container";
import PropTypes from "prop-types";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Snackbar from "../components/deleteSnackBar";

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(2),
    width: "100%",
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular
  },
  image: {
    width: 200,
    height: 220
  },
  img: {
    margin: "auto",
    display: "block",
    maxWidth: "100%",
    maxHeight: "100%"
  }
}));

function TabContainer(props) {
  return (
    <Typography component="div" style={{ padding: 8 * 3 }}>
      {props.children}
    </Typography>
  );
}

TabContainer.propTypes = {
  children: PropTypes.node.isRequired
};

export default function WishList(props) {
  //console.log(props.searchResult);
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  function handleChange(event, newValue) {
    setValue(newValue);
  }

  function PrintDescription() {
    return (
      <React.Fragment>
        <ul>
          {props.searchResult.description.map(description => (
            <li>{description}</li>
          ))}
        </ul>
      </React.Fragment>
    );
  }

  function PrintUrlButton() {
    return (
      <React.Fragment>
        {props.searchResult.websites.map(urlbutton => (
          <Typography variant="body2" gutterBottom>
            <Link
              href={urlbutton.product_link}
              target="_blank"
              rel="noreferrer"
              color="inherit"
            >
              <Button
                size="small"
                variant="contained"
                color="primary"
                fullWidth
              >
                {urlbutton.website_name} <br />
                {urlbutton.price} ৳
                <br />
                {urlbutton.status}
              </Button>
            </Link>
          </Typography>
        ))}
      </React.Fragment>
    );
  }

  function PrintImage() {
    return (
      <React.Fragment>
        {props.searchResult.websites.map(site => (
          <img
            className={classes.image}
            alt={site.website_name}
            src={site.img_link}
          />
        ))}
      </React.Fragment>
    );
  }

  return (
    <Container component="main">
      <div className={classes.root}>
        <ExpansionPanel>
          <ExpansionPanelSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
            id="panel1a-header"
          >
            <Grid container spacing={2}>
              <Grid item>
                <ButtonBase className={classes.image}>
                  <img
                    className={classes.img}
                    alt=""
                    src={props.searchResult.websites[0].img_link}
                  />
                </ButtonBase>
              </Grid>
              <Grid item xs={12} sm container>
                <Grid
                  item
                  xs
                  container
                  wrap="nowrap"
                  direction="column"
                  spacing={2}
                >
                  <Grid item xs zeroMinWidth>
                    <Typography gutterBottom variant="subtitle1">
                      <b>{props.searchResult.product_title}</b>
                    </Typography>
                    <Typography variant="body2" gutterBottom>
                      <PrintDescription />
                    </Typography>
                  </Grid>
                </Grid>
                <center>
                  <Grid item xs container direction="column" spacing={2}>
                    <Grid item xs borderBottom={5}>
                      <PrintUrlButton />
                      <Typography variant="body2" gutterBottom>
                        <Button
                          size="small"
                          variant="contained"
                          color="primary"
                        >
                          More Deals ↓
                        </Button>
                      </Typography>
                    </Grid>
                  </Grid>
                </center>
                <Grid item xs container direction="column" spacing={2}>
                  <Grid item xs>
                    <Typography
                      style={{ marginTop: 65 }}
                      variant="body2"
                      gutterBottom
                    >
                      <Link
                        href={props.searchResult.websites[0].product_link}
                        target="_blank"
                        rel="noreferrer"
                        color="inherit"
                      >
                        <Button
                          size="large"
                          variant="contained"
                          color="primary"
                          fullWidth
                        >
                          Best Deal →
                        </Button>
                      </Link>
                    </Typography>
                    {props.isAuthenticated ? (
                      <Typography variant="body2" gutterBottom>
                        <Button
                          size="small"
                          variant="contained"
                          color="secondary"
                          fullWidth
                        >
                          <Snackbar {...props.searchResult} />
                        </Button>
                      </Typography>
                    ) : (
                      ""
                    )}
                  </Grid>
                </Grid>
              </Grid>
            </Grid>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <AppBar position="static">
              <Tabs value={value} onChange={handleChange}>
                <Tab label="Info" />
                <Tab label="Photos" />
                <Tab label="Deals" />
              </Tabs>
            </AppBar>
          </ExpansionPanelDetails>
          {value === 0 && (
            <TabContainer>
              <PrintDescription />
            </TabContainer>
          )}
          {value === 1 && (
            <TabContainer>
              <PrintImage />
            </TabContainer>
          )}
          {value === 2 && (
            <TabContainer>
              <PrintUrlButton />
            </TabContainer>
          )}
        </ExpansionPanel>
      </div>
    </Container>
  );
}
