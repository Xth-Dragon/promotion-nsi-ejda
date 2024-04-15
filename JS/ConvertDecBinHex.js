(function () {

    'use strict';
  
    var SgConverter = function () {
      var that = this;
  
      this.converters = ['decimal', 'hexadecimal', 'binary'];
      this.inputElements = {};
  
      this.decimalToHexadecimal = function (decimalValue) {
        return parseInt(decimalValue, 10).toString(16);
      };
  
      this.decimalToBinary = function (decimalValue) {
        return parseInt(decimalValue, 10).toString(2);
      };
  
      this.hexadecimalToDecimal = function (hexadecimalValue) {
        return parseInt(hexadecimalValue, 16);
      };
  
      this.hexadecimalToBinary = function (hexadecimalValue) {
        return (parseInt(hexadecimalValue, 16)).toString(2);
      };
  
      this.binaryToDecimal = function (binaryValue) {
        return parseInt(binaryValue, 2);
      };
  
      this.binaryToHexadecimal = function (binaryValue) {
        return (parseInt(binaryValue, 2)).toString(16);
      };
  
      this.convert = function (sourceType) {
        var sourceValue = this.inputElements[sourceType].value;
        this.converters.forEach(function (converter) {
          if (converter !== sourceType) {
            var ucConverter = converter.charAt(0).toUpperCase() + converter.slice(1);
            var converterMethod = sourceType + 'To' + ucConverter;
            that.inputElements[converter].value = that[converterMethod](sourceValue);
          }
        });
      }; // convert
  
      this.update = function (event) {
        that.convert(event.target.id);
      };
    }; // onEnterKey
  
    document.addEventListener('DOMContentLoaded', function () {
      document.getElementById('decimal').focus();
      var sgConverter = new SgConverter();
      sgConverter.converters.forEach(function (converter) {
        sgConverter.inputElements[converter] = document.getElementById(converter);
        document.getElementById(converter).nextElementSibling.addEventListener('click', function () {
          sgConverter.convert(converter);
        }, false );
  
        ['keyup', 'change'].forEach(function (event) {
          document.getElementById(converter).addEventListener(event, sgConverter.update, false);
        });
  
      });
    }); // DOMContentLoaded
  
  }()); // IIFE