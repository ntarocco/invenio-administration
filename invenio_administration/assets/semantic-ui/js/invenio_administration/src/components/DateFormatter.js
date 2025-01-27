/*
 * This file is part of Invenio.
 * Copyright (C) 2022 CERN.
 *
 * Invenio is free software; you can redistribute it and/or modify it
 * under the terms of the MIT License; see LICENSE file for more details.
 */

import React from "react";
import PropTypes from "prop-types";
import { DateTime } from "luxon";

class DateFormatter extends React.Component {
  render() {
    const { value } = this.props;

    const date = DateTime.fromISO(value);
    return (
      <p data-testid="date-formatter">{date.toLocaleString(DateTime.DATETIME_MED)}</p>
    );
  }
}

DateFormatter.propTypes = {
  value: PropTypes.string.isRequired,
};

export default DateFormatter;
