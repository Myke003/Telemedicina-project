import React from 'react';

function InputGroup({type, placeholder, icon}) {
  return (
    <div className="input-group">
      <span className="input-group-text" id="addon-wrapping">
      <i className={`bi ${icon}`}></i>
      </span>
      <input type={type} className="form-control" placeholder={placeholder} aria-label={placeholder} aria-describedby="addon-wrapping" />
    </div>
  );
}

export default InputGroup;