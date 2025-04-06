import React, {  } from 'react';
import './App.css';
import RubbishCollectionDay from './RubbishCollectionDay';
import { ThemeProvider } from '@emotion/react';
import { createTheme, CssBaseline } from '@mui/material';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const App: React.FC = () => {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <RubbishCollectionDay />
    </ThemeProvider>
  )
};

export default App;
