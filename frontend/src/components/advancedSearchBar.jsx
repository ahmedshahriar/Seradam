import React from "react";
import deburr from "lodash/deburr";
import Downshift from "downshift";
import Paper from "@material-ui/core/Paper";
import MenuItem from "@material-ui/core/MenuItem";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
//brand&site
import Input from "@material-ui/core/Input";
import InputLabel from "@material-ui/core/InputLabel";
import FormControl from "@material-ui/core/FormControl";
import ListItemText from "@material-ui/core/ListItemText";
import Select from "@material-ui/core/Select";
import Checkbox from "@material-ui/core/Checkbox";

const useStyles = makeStyles(theme => ({
  "@global": {
    body: {
      backgroundColor: theme.palette.common.white
    }
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: "100%",
    maxWidth: "100%"
  },
  container: {
    flexGrow: 1,
    position: "relative"
  },
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center"
  },
  paper1: {
    position: "absolute",
    zIndex: 1,
    marginTop: theme.spacing(1),
    left: 0,
    right: 0
  },
  inputRoot: {
    flexWrap: "wrap"
  },
  inputInput: {
    width: "auto",
    flexGrow: 1
  },
  form: {
    width: "100%",
    marginTop: theme.spacing(3)
  },
  submit: {
    margin: theme.spacing(1)
  }
}));

function renderInput(inputProps) {
  const { InputProps, classes, ref, ...other } = inputProps;

  return (
    <TextField
      variant="outlined"
      fullWidth
      id="category"
      label="Category"
      name="category"
      placeholder="Can be left empty"
      InputProps={{
        inputRef: ref,
        classes: {
          root: classes.inputRoot,
          input: classes.inputInput
        },
        ...InputProps
      }}
      {...other}
    />
  );
}

function renderSuggestion(suggestionProps) {
  const {
    suggestion,
    index,
    itemProps,
    highlightedIndex,
    selectedItem
  } = suggestionProps;
  const isHighlighted = highlightedIndex === index;
  const isSelected = (selectedItem || "").indexOf(suggestion.label) > -1;

  return (
    <MenuItem
      {...itemProps}
      key={suggestion.label}
      selected={isHighlighted}
      component="div"
      style={{
        fontWeight: isSelected ? 500 : 400
      }}
    >
      {suggestion.label}
    </MenuItem>
  );
}

function getSuggestions(suggestions, value, { showEmpty = false } = {}) {
  const inputValue = deburr(value.trim()).toLowerCase();
  const inputLength = inputValue.length;
  let count = 0;

  return inputLength === 0 && !showEmpty
    ? []
    : suggestions.filter(suggestion => {
        const keep =
          count < 5 &&
          suggestion.label.slice(0, inputLength).toLowerCase() === inputValue;

        if (keep) {
          count += 1;
        }

        return keep;
      });
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

export default function AdvancedSearchBar(props) {
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

  return (
    <Container component="main">
      <div className={classes.paper}>
        <form className={classes.form} noValidate>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={4}>
              <TextField
                name="search"
                variant="outlined"
                required
                fullWidth
                id="search"
                label="Search"
                placeholder="Search here e.g Ram"
              />
            </Grid>
            <Grid item xs={12} sm={2}>
              <Downshift id="downshift-options">
                {({
                  clearSelection,
                  getInputProps,
                  getItemProps,
                  getLabelProps,
                  getMenuProps,
                  highlightedIndex,
                  inputValue,
                  isOpen,
                  openMenu,
                  selectedItem
                }) => {
                  const {
                    onBlur,
                    onChange,
                    onFocus,
                    ...inputProps
                  } = getInputProps({
                    onChange: event => {
                      if (event.target.value === "") {
                        clearSelection();
                      }
                    },
                    onFocus: openMenu
                  });

                  return (
                    <div className={classes.container}>
                      {renderInput({
                        fullWidth: true,
                        classes,
                        InputLabelProps: getLabelProps({ shrink: true }),
                        InputProps: { onBlur, onChange, onFocus },
                        inputProps
                      })}

                      <div {...getMenuProps()}>
                        {isOpen ? (
                          <Paper className={classes.paper1} square>
                            {getSuggestions(props.category, inputValue, {
                              showEmpty: true
                            }).map((suggestion, index) =>
                              renderSuggestion({
                                suggestion,
                                index,
                                itemProps: getItemProps({
                                  item: suggestion.label
                                }),
                                highlightedIndex,
                                selectedItem
                              })
                            )}
                          </Paper>
                        ) : null}
                      </div>
                    </div>
                  );
                }}
              </Downshift>
            </Grid>
            <Grid item xs={12} sm={2}>
              <FormControl className={classes.formControl}>
                <InputLabel htmlFor="select-multiple-checkbox">
                  Brand
                </InputLabel>
                <Select
                  name="brand"
                  multiple
                  value={brandName}
                  onChange={handleChangeBrand}
                  input={<Input id="select-multiple-checkbox" />}
                  renderValue={selected => selected.join(", ")}
                  MenuProps={MenuProps}
                >
                  {props.allBrandNames.map(name => (
                    <MenuItem key={name.brand} value={name.brand}>
                      <Checkbox checked={brandName.indexOf(name.brand) > -1} />
                      <ListItemText primary={name.brand} />
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>
            <Grid item xs={12} sm={2}>
              <FormControl className={classes.formControl}>
                <InputLabel htmlFor="select-multiple-checkbox">Site</InputLabel>
                <Select
                  multiple
                  name="site"
                  value={siteName}
                  onChange={handleChangeSite}
                  input={<Input id="select-multiple-checkbox" />}
                  renderValue={selected => selected.join(", ")}
                  MenuProps={MenuProps}
                >
                  {props.allSiteNames.map(name => (
                    <MenuItem key={name} value={name}>
                      <Checkbox checked={siteName.indexOf(name) > -1} />
                      <ListItemText primary={name} />
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>
            <Grid item xs={12} sm={2}>
              <Button
                type="submit"
                fullWidth
                variant="contained"
                color="primary"
                className={classes.submit}
              >
                Search
              </Button>
            </Grid>
          </Grid>
        </form>
      </div>
    </Container>
  );
}
