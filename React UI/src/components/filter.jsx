import React from "react";
//price
import PropTypes from "prop-types";
import { withStyles, makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Slider from "@material-ui/core/Slider";
import Typography from "@material-ui/core/Typography";
import Tooltip from "@material-ui/core/Tooltip";
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
import OutlinedInput from "@material-ui/core/OutlinedInput";
import FilledInput from "@material-ui/core/FilledInput";
import FormHelperText from "@material-ui/core/FormHelperText";
import NativeSelect from "@material-ui/core/NativeSelect";

//price
const useStyles = makeStyles(theme => ({
  root: {
    width: 300 + 24 * 2,
    padding: 15
  },
  brand: {
    width: 212 + 24 * 2,
    padding: 15
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: 212,
    maxWidth: 212
  },
  custom: {
    padding: theme.spacing(2),
    width: "100%",
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper
  }
}));

function ValueLabelComponent(props) {
  const { children, open, value } = props;

  const popperRef = React.useRef(null);
  React.useEffect(() => {
    if (popperRef.current) {
      popperRef.current.update();
    }
  });

  return (
    <Tooltip
      PopperProps={{
        popperRef
      }}
      open={open}
      enterTouchDelay={0}
      placement="top"
      title={value}
    >
      {children}
    </Tooltip>
  );
}

ValueLabelComponent.propTypes = {
  children: PropTypes.element.isRequired,
  open: PropTypes.bool.isRequired,
  value: PropTypes.number.isRequired
};

const PrettoSlider = withStyles({
  root: {
    color: "#52af77",
    height: 8
  },
  thumb: {
    height: 24,
    width: 24,
    backgroundColor: "#fff",
    border: "2px solid currentColor",
    marginTop: -8,
    marginLeft: -12,
    "&:focus,&:hover,&$active": {
      boxShadow: "inherit"
    }
  },
  active: {},
  valueLabel: {
    left: "calc(-50% + 4px)"
  },
  track: {
    height: 8,
    borderRadius: 4
  },
  rail: {
    height: 8,
    borderRadius: 4
  }
})(Slider);

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
const brandNames = [
  "Intel",
  "AMD",
  "Asrock",
  "Asus",
  "Gigabyte",
  "Corsair",
  "Seasonic",
  "Samsung",
  "Sandisk",
  "Seagate"
];
//site
const siteNames = ["StarTech", "Pickaboo", "Kiksha", "Google"];

export default function CustomizedSlider() {
  const classes = useStyles();

  const [brandName, setbrandName] = React.useState([]); //brand
  function handleChangeBrand(event) {
    //brand
    setbrandName(event.target.value);
  }

  const [siteName, setsiteName] = React.useState([]); //site
  function handleChangeSite(event) {
    //site
    setsiteName(event.target.value);
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

  return (
    <Container component="main">
      <div className={classes.custom}>
        <Grid container spacing={2}>
          <Grid item>
            <Paper className={classes.root}>
              <Typography gutterBottom>Price</Typography>
              <PrettoSlider
                valueLabelDisplay="auto"
                aria-label="Pretto slider"
                defaultValue={20}
              />
            </Paper>
          </Grid>
          <Grid item>
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
                  {brandNames.map(name => (
                    <MenuItem key={name} value={name}>
                      <Checkbox checked={brandName.indexOf(name) > -1} />
                      <ListItemText primary={name} />
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Paper>
          </Grid>

          <Grid item>
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
                  {siteNames.map(name => (
                    <MenuItem key={name} value={name}>
                      <Checkbox checked={siteName.indexOf(name) > -1} />
                      <ListItemText primary={name} />
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Paper>
          </Grid>
          <Grid item>
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
