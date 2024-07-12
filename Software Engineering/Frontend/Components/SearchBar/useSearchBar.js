import React, { useEffect, useState } from "react";
import "./SearchBar.css";
import "@fontsource/inter";

function useSearchBar() {
  const [searchText, setSearchText] = useState("");
  const [prev, setPrev] = useState("");

  const onValueChange = (e) => {
    setPrev(searchText);
    setSearchText(e.target.value);
  };

  useEffect(() => {}, [searchText]);

  return {
    searchText,
    prev,
    render: (
      <div>
        <div className="sb-search">
          <input
            className="sb-search-input"
            type="search"
            onChange={onValueChange}
            placeholder="SEARCH MOVIES"
          ></input>
        </div>
      </div>
    ),
  };
}

export default useSearchBar;
