import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import ButtonBase from "@material-ui/core/ButtonBase";
import Button from "@material-ui/core/Button";
import Link from "@material-ui/core/Link";

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1
  },
  paper: {
    padding: theme.spacing(2),
    margin: "auto",
    maxWidth: 800
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

export default function ComplexGrid() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Paper className={classes.paper}>
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
                    <Button size="small" variant="contained" color="primary">
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
      </Paper>
    </div>
  );
}
