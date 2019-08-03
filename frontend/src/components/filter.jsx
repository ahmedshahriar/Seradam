import React from "react";
//price
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Slider from "@material-ui/core/Slider";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
//brand&site
import Input from "@material-ui/core/Input";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import ListItemText from "@material-ui/core/ListItemText";
import Select from "@material-ui/core/Select";
import Checkbox from "@material-ui/core/Checkbox";
//sortby
import NativeSelect from "@material-ui/core/NativeSelect";

const useStyles = makeStyles(theme => ({
  root: {
    padding: 15
  },
  brand: {
    padding: 15
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: "100%",
    maxWidth: "100%"
  },
  custom: {
    padding: theme.spacing(2),
    width: "100%",
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper
  }
}));

//price
function pricevaluetext(value) {
  return `${value}°C`;
}

//brand
const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250
    }
  }
};

let flag = 0;

export default function Filter(props) {
  //console.log(props.filterPrice);
  const classes = useStyles();
  let min = props.filterPrice[0];
  let max = props.filterPrice[1];
  //price
  const [price, setPrice] = React.useState([min, max]);
  const handleChangePrice = (event, newValue) => {
    setPrice(newValue);
    flag = 1;
  };

  //brand
  const [brandName, setBrandName] = React.useState(props.filterBrandNames);
  function handleChangeBrand(event) {
    setBrandName(event.target.value);
    flag = 1;
    //console.log(brandName);
  }

  //site
  const [siteName, setsiteName] = React.useState(props.filterSiteNames);
  function handleChangeSite(event) {
    setsiteName(event.target.value);
    flag = 1;
    //console.log(siteName);
  }

  //sortby
  const [sortby, setSortBy] = React.useState({
    sort: ""
  });

  const handleChangeSortby = name => event => {
    setSortBy({
      ...sortby,
      [name]: event.target.value
    });
  };

  if (flag) {
    props.filterResults(price, brandName, siteName);
    flag = 0;
  }

  return (
    <Container component="main">
      <div className={classes.custom}>
        <Grid container spacing={2}>
          <Grid item xs={12} sm={3}>
            <Paper className={classes.root}>
              <Typography gutterBottom>Price</Typography>
              <Slider
                min={props.filterPrice[0]}
                max={props.filterPrice[1]}
                value={price}
                onChange={handleChangePrice}
                valueLabelDisplay="auto"
                aria-labelledby="range-slider"
                getAriaValueText={pricevaluetext}
              />
            </Paper>
          </Grid>
          <Grid item xs={12} sm={3}>
            <Paper className={classes.brand}>
              <FormControl className={classes.formControl}>
                <InputLabel htmlFor="select-multiple-checkbox">
                  Brand
                </InputLabel>
                <Select
                  multiple
                  value={brandName}
                  onChange={handleChangeBrand}
                  input={<Input id="select-multiple-checkbox" />}
                  renderValue={selected => selected.join(", ")}
                  MenuProps={MenuProps}
                >
                  {props.filterBrandNames.map(name => (
                    <MenuItem key={name} value={name}>
                      <Checkbox checked={brandName.indexOf(name) > -1} />
                      <ListItemText primary={name} />
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Paper>
          </Grid>

          <Grid item xs={12} sm={3}>
            <Paper className={classes.brand}>
              <FormControl className={classes.formControl}>
                <InputLabel htmlFor="select-multiple-checkbox">Site</InputLabel>
                <Select
                  multiple
                  value={siteName}
                  onChange={handleChangeSite}
                  input={<Input id="select-multiple-checkbox" />}
                  renderValue={selected => selected.join(", ")}
                  MenuProps={MenuProps}
                >
                  {props.filterSiteNames.map(name => (
                    <MenuItem key={name} value={name}>
                      <Checkbox checked={siteName.indexOf(name) > -1} />
                      <ListItemText primary={name} />
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Paper>
          </Grid>
          <Grid item xs={12} sm={3}>
            <Paper className={classes.brand}>
              <FormControl className={classes.formControl}>
                <InputLabel shrink htmlFor="sort-native-label-placeholder">
                  Sort By
                </InputLabel>
                <NativeSelect
                  value={sortby.sort}
                  onChange={handleChangeSortby("sort")}
                  input={
                    <Input name="sort" id="sort-native-label-placeholder" />
                  }
                >
                  <option value={10}>A-Z</option>
                  <option value={20}>Price</option>
                  <option value={30}>Date Modified</option>
                </NativeSelect>
              </FormControl>
            </Paper>
          </Grid>
        </Grid>
      </div>
    </Container>
  );
}
