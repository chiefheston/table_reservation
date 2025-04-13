from datetime import datetime, timedelta

from app.models import Reservation
from app.services.constants import RESERVATION_BUSY


async def get_overlapping_reservations(
    reservations_list: list[Reservation],
    reservation_start_time: datetime,
    reservation_end_time: datetime,
) -> list[Reservation]:
    """Gets a list of created reservations that can be overlapped

    Args:
        reserevation_list (list[Reservation]): Reservation object
        reservation_start_time (datetime): Starting time of reservation to create
        reservation_end_time (datetime): End time of reservation to create
        session (AsyncSession): Session object
        
    Returns:
        None
    """
    st = reservation_start_time  # Reservation start time
    et = reservation_end_time

    overlapping_reservations_list = []

    for rsr in reservations_list:  # reservation in reservations
        rsr_st = rsr.reservation_time  # Reservation start time
        delta = timedelta(minutes=rsr.duration_minutes)  # Time delta
        rsr_et = rsr_st + delta  # Reservation end time
        rsr.reservation_time_end = (
            rsr_et  # Reservation end time, extra field for check overlapping
        )
        if not (
            (st < rsr_st > et)
            and (st < rsr_et > et)
            or (st > rsr_st < et)
            and (st > rsr_et < et)
        ):
            overlapping_reservations_list.append(
                RESERVATION_BUSY.format(
                    rsr.customer_name,
                    rsr.reservation_time,
                    rsr.reservation_time_end,
                )
            )

    return overlapping_reservations_list
