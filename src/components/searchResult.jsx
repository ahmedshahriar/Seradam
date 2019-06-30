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

export default function SimpleExpansionPanel() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  function handleChange(event, newValue) {
    setValue(newValue);
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
                    alt="complex"
                    src="https://picsum.photos/220"
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
                      Ram 16 GB
                    </Typography>
                    <Typography variant="body2" gutterBottom>
                      5400 rpm high tech
                    </Typography>
                    <Typography variant="body2" color="textSecondary">
                      Ratings: 4
                    </Typography>
                  </Grid>
                </Grid>
                <center>
                  <Grid item xs container direction="column" spacing={2}>
                    <Grid item xs borderBottom={5}>
                      <Typography variant="body2" gutterBottom>
                        <Button
                          size="small"
                          variant="contained"
                          color="primary"
                          fullWidth
                        >
                          <Link href="https://google.com/" color="inherit">
                            StarTech <br />
                            50$
                          </Link>
                        </Button>
                      </Typography>
                      <Typography variant="body2" gutterBottom>
                        <Button
                          size="auto"
                          variant="contained"
                          color="primary"
                          fullWidth
                        >
                          <Link href="https://google.com/" color="inherit">
                            Ryans <br />
                            60$
                          </Link>
                        </Button>
                      </Typography>
                      <Typography variant="body2" gutterBottom>
                        <Button
                          size="small"
                          variant="contained"
                          color="primary"
                          fullWidth
                        >
                          <Link href="https://google.com/" color="inherit">
                            Pickaboo <br />
                            65$
                          </Link>
                        </Button>
                      </Typography>
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
                      style={{ marginTop: 100 }}
                      variant="body2"
                      gutterBottom
                    >
                      <Button
                        size="large"
                        variant="contained"
                        color="primary"
                        fullWidth
                      >
                        <Link href="https://google.com/" color="inherit">
                          Best Deal →
                        </Link>
                      </Button>
                    </Typography>
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
          {value === 0 && <TabContainer>Info</TabContainer>}
          {value === 1 && <TabContainer>Photos</TabContainer>}
          {value === 2 && <TabContainer>Deals</TabContainer>}
        </ExpansionPanel>
      </div>
    </Container>
  );
}
