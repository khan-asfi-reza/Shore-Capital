const defaultTheme = require("tailwindcss");
module.exports = {
  purge: [
      '../templates/**/*.html',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      screens: {
        'xs': '475px',
        ...defaultTheme.screens,
      },
      opacity:{
        85: "85%"
      },
      colors:{
        primary: "#0E2031",
        secondary: "#19A6E8",
        secondaryDeep: "#0984BE",
        secondaryLight: "#D7F0FC",
        secondaryOverlay: "#67C5F2",
        textLight: "#CBCBCB",
        textDark: "#4d4d4d",
        headDark: "#292929",
        overlayDark: "#2D2C2C",
        bgLight: "#FBFBFB",
        overlayBlue: "#0E2031"
      },
      gridTemplateRows: {
        '70vh': '70vh',
        '50vh': '40vh',
        '30vh': '30vh'
      },
      height:{
        ...defaultTheme.height,
        '70vh': '70vh',
        '80vh': '80vh',
        'screen-extended': '112vh',
      },
      width: {
        '27%' : '27%',
        '30%' : '30%',
      },
      zIndex:{
        '100': '100'
      }
    },
  },
  variants: {
    extend: {
      borderRadius: ['hover']
    },
  },
  plugins: [],
}
