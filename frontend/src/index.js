import React from "react";
import ReactDOM from "react-dom";
import Home from "./home";
import * as serviceWorker from "./serviceWorker";
import { createStore, compose, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import thunk from 'redux-thunk';

import reducer from './store/reducers/auth';

const composeEnhances = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const store = createStore(reducer, composeEnhances(
    applyMiddleware(thunk)
));

const app = (
    <Provider store={store}>
        <Home />
    </Provider>
)

ReactDOM.render(app, document.getElementById('root'));
serviceWorker.unregister();
